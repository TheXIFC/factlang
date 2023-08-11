from node import *
from scope import *
import static_calc as sc
import registers as regs
from values import Const


class _MatchBreak(Exception):
    pass


reverse_op = {
    '>': '<=',
    '<': '>=',
    '>=': '<',
    '<=': '>',
    '==': '!=',
    '!=': '==',
}


# node types for custom children handling
custom_nodes = [NodeType.If, NodeType.IfElse, NodeType.While]


def parse_node(node: Node, command_list: list, scope: Scope, curr_scope: str, args: dict):

    if args is None:
        args = {}
    new_args = args.copy()

    custom_child_handle = False
    if node.type in custom_nodes:
        custom_child_handle = True

    cl = []  # current command list

    child_commands = []
    if not custom_child_handle:
        for child in node.children:
            if isinstance(child, Node):
                new_cl = []
                parse_node(child, new_cl, scope, curr_scope, new_args)
                child_commands.append(new_cl)

    try:
        match node.type:
            case NodeType.Script:
                pass
            case NodeType.StatementList:
                pass
            case NodeType.EmptyBlock:
                print("empty_block")
            case NodeType.Empty:
                print("empty")
            case NodeType.Const:
                node.value = Const(node.leaf[0], node.leaf[1])
                node.const = True
            case NodeType.Var:
                name = node.leaf
                if (var := scope.get_var(name)) is None:
                    raise Exception(f"Unknown variable {name}")
                node.value = var
            case NodeType.UnaryOp:
                op = node.leaf
                if node.children[0].const:
                    node.value = sc.unary_op(op, node.children[0].value)
                    node.const = True
                    raise _MatchBreak()

                if op == '+':
                    node.value = node.children[0].value
                    raise _MatchBreak()

                tmp_var = scope.alloc_temp(node)

                if op == '-':
                    cl.append({'op': 'write', 'to': regs.unary_minus, 'from': node.children[0].value})
                    cl.append({'op': 'write', 'to': tmp_var, 'from': regs.unary_minus})

            case NodeType.Exp:
                if node.children[0].const and node.children[1].const:
                    node.value = sc.exp(node.children[0].value, node.children[1].value)
                    node.const = True
                    raise _MatchBreak()

                cl.append({'op': 'write', 'to': regs.exp, 'from': node.children[1].value})

                res = scope.alloc_temp(node)
                if node.children[0].const:
                    var = scope.alloc_temp(node)
                    cl.append({'op': 'write', 'to': var, 'from': node.children[0].value})
                else:
                    var = node.children[0].value

                cl.append({'op': 'exp', 'from': var})
                cl.append({'op': 'write', 'to': res, 'from': regs.exp})
                node.value = res

            case NodeType.Mul:
                op = node.leaf
                if node.children[0].const and node.children[1].const:
                    node.value = sc.mul(node.children[0].value, node.children[1].value, op)
                    node.const = True
                    raise _MatchBreak()

                # before optimizing remember, that it's not only multiplication, but also division and modulo

                if op == '*':
                    reg = regs.mul
                elif op == '/':
                    reg = regs.div
                elif op == '%':
                    reg = regs.mod
                else:
                    raise Exception("Unknown op")

                cl.append({'op': 'write', 'to': reg, 'from': node.children[1].value})

                res = scope.alloc_temp(node)
                if node.children[0].const:
                    var = scope.alloc_temp(node)
                    cl.append({'op': 'write', 'to': var, 'from': node.children[0].value})
                else:
                    var = node.children[0].value

                cl.append({'op': op, 'from': var})
                cl.append({'op': 'write', 'to': res, 'from': reg})
                node.value = res

            case NodeType.Add:
                op = node.leaf
                # if both arguments are constant
                if node.children[0].const and node.children[1].const:
                    node.value = sc.add(node.children[0].value, node.children[1].value, op)
                    node.const = True
                    raise _MatchBreak()

                res = scope.alloc_temp(node)
                # if one of the arguments is constant (minus is tricky)
                if node.children[0].const or node.children[1].const:
                    if op == '+':
                        cl.append({'op': 'write', 'to': res, 'from': (node.children[0].value, node.children[1].value)})
                    elif op == '-':
                        if node.children[0].const:
                            cl.append({'op': 'write', 'to': regs.unary_minus, 'from': node.children[1].value})
                            cl.append({'op': 'write', 'to': res, 'from': (node.children[0].value, regs.unary_minus)})
                        elif node.children[1].const:
                            val = sc.unary_op('-', node.children[1].value)
                            cl.append({'op': 'write', 'to': res, 'from': (node.children[0].value, val)})
                    node.value = res
                    raise _MatchBreak()

                # if both arguments are variables
                cl.append({'op': 'write', 'to': res, 'from': node.children[0].value})
                if op == '+':
                    cl.append({'op': 'write_add', 'to': res, 'from': node.children[1].value})
                elif op == '-':
                    cl.append({'op': 'write', 'to': regs.unary_minus, 'from': node.children[1].value})
                    cl.append({'op': 'write_add', 'to': res, 'from': regs.unary_minus})

                node.value = res

            case NodeType.Assign:
                name = node.children[0]
                expression = node.children[1]
                op = node.leaf

                var = scope.get_var(name, create=curr_scope)

                # TODO add other operations
                command = {'op': 'write', 'to': var, 'from': expression.value}

                cl.append(command)

            case NodeType.Relational:
                op = node.leaf

                if node.children[0].const and node.children[1].const:
                    # TODO
                    raise _MatchBreak()

                if node.children[0].const:
                    # swapping arguments for optimization
                    arg0 = node.children[1]
                    arg1 = node.children[0]

                    if '>' in op:
                        op = op.replace('>', '<')
                    else:
                        op = op.replace('<', '>')
                else:
                    arg0 = node.children[0]
                    arg1 = node.children[1]

                res = scope.alloc_temp(node)

                if op == '<':
                    reg = regs.less_than
                elif op == '<=':
                    reg = regs.less_eq
                elif op == '>':
                    reg = regs.gr_than
                elif op == '<=':
                    reg = regs.gr_eq
                else:
                    raise Exception("Unknown op")

                cl.append({'op': 'write', 'to': reg, 'from': arg1.value})
                cl.append({'op': op, 'from': arg0.value})
                cl.append({'op': 'write', 'to': res, 'from': reg})

                node.value = res

            case NodeType.Equality:
                op = node.leaf

                if node.children[0].const and node.children[1].const:
                    # TODO
                    raise _MatchBreak()

                if node.children[0].const:
                    # swapping arguments for optimization
                    arg0 = node.children[1]
                    arg1 = node.children[0]
                else:
                    arg0 = node.children[0]
                    arg1 = node.children[1]

                res = scope.alloc_temp(node)

                if op == '==':
                    reg = regs.eq
                elif op == '!=':
                    reg = regs.neq
                else:
                    raise Exception("Unknown op")

                cl.append({'op': 'write', 'to': reg, 'from': arg1.value})
                cl.append({'op': op, 'from': arg0.value})
                cl.append({'op': 'write', 'to': res, 'from': reg})

                node.value = res

            case NodeType.If:
                condition_node = node.leaf
                condition_cl = []
                parse_node(condition_node, condition_cl, scope, curr_scope, new_args)
                condition_node.cleanup(scope)

                if_end_label = {'label': 'if_end'}
                cl.extend(condition_cl)
                cl.append({'op': 'c_jump', 'condition': 'is_zero', 'destination': if_end_label, 'from': condition_node.value})

                inner_scope = scope.copy()
                body_cl = []
                body_node = node.children[0]
                parse_node(body_node, body_cl, inner_scope, curr_scope, new_args)
                cl.extend(body_cl)
                cl.append(if_end_label)

            case NodeType.IfElse:
                condition_node = node.leaf
                condition_cl = []
                parse_node(condition_node, condition_cl, scope, curr_scope, new_args)
                condition_node.cleanup(scope)

                if_end_label = {'label': 'if_end'}
                else_label = {'label': 'else'}
                cl.extend(condition_cl)
                cl.append({'op': 'c_jump', 'condition': 'is_zero', 'destination': else_label, 'from': condition_node.value})

                inner_scope = scope.copy()
                true_cl = []
                true_node = node.children[0]
                parse_node(true_node, true_cl, inner_scope, curr_scope, new_args)
                cl.extend(true_cl)
                cl.append({'op': 'jump', 'destination': if_end_label})

                cl.append(else_label)
                inner_scope = scope.copy()
                false_cl = []
                false_node = node.children[1]
                parse_node(false_node, false_cl, inner_scope, curr_scope, new_args)
                cl.extend(false_cl)
                cl.append(if_end_label)

            case NodeType.While:
                condition_node = node.leaf
                condition_cl = []
                parse_node(condition_node, condition_cl, scope, curr_scope, new_args)

                while_start_label = {'label': 'while_start'}
                while_end_label = {'label': 'while_end'}

                new_args['continue'] = while_start_label
                new_args['breaK'] = while_end_label

                cl.append(while_start_label)
                cl.extend(condition_cl)
                cl.append({'op': 'c_jump', 'condition': 'is_zero', 'destination': while_end_label, 'from': condition_node.value})

                condition_node.cleanup(scope)
                inner_scope = scope.copy()
                body_cl = []
                body_node = node.children[0]
                parse_node(body_node, body_cl, inner_scope, curr_scope, new_args)
                cl.extend(body_cl)
                cl.append({'op': 'jump', 'destination': while_start_label})
                cl.append(while_end_label)

            case NodeType.Continue:
                if 'continue' not in args:
                    raise Exception("Continue use outside of loop")
                continue_label = args['continue']
                cl.append({'op': 'jump', 'destination': continue_label})

            case NodeType.Break:
                if 'break' not in args:
                    raise Exception("Break use outside of loop")
                break_label = args['break']
                cl.append({'op': 'jump', 'destination': break_label})

            case _:
                print("Unhandled node type " + node.type.value)
    except _MatchBreak:
        pass

    for child in node.children:
        if isinstance(child, Node):
            node.cleanup(scope)

    if not custom_child_handle:
        for child_cl in child_commands:
            command_list.extend(child_cl)
    command_list.extend(cl)

