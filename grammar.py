import ply.lex as lex
import lexer
from lexer import tokens
import logging

from ply import yacc

from node import *

logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)

# ---Grammar rules---
precedence = (
    # ('nonassoc', '+', '-'),  # Nonassociative operators
    # ('left', '+', '-'),
    # ('left', '*', '/'),
    # ('right', 'UMINUS'),  # Unary minus operator
)


# Error rule for syntax errors
def p_error(p):
    print(f"Unexpected symbol {p.value} at line {p.lineno}")


def p_script(p):
    """
    script : script_entity
    | script script_entity
    """
    if len(p) == 2:
        p[0] = Node(NodeType.Script, None, [p[1]])
    else:
        p[1].children.append(p[2])
        p[0] = p[1]


def p_script_entity(p):
    """script_entity : statement"""
    p[0] = p[1]


def p_statement_list(p):
    """
    statement_list : statement
    | statement_list statement
    """

    if len(p) == 2:
        p[0] = Node(NodeType.StatementList, None, [p[1]])
    else:
        p[1].children.append(p[2])
        p[0] = p[1]


def p_compound_statement(p):
    """
    compound_statement : '{' '}'
    | '{' statement_list '}'
    """
    if len(p) == 3:
        p[0] = Node(NodeType.EmptyBlock)
    else:
        p[0] = p[2]


def p_unit_exp(p):
    """
    primary_expression : value
    unary_expression : primary_expression
    exponential_expression : unary_expression
    multiplicative_expression : exponential_expression
    additive_expression : multiplicative_expression
    shift_expression : additive_expression
    relational_expression : shift_expression
    equality_expression : relational_expression

    assignment_expression : equality_expression
    expression : assignment_expression
    expression_statement : expression ';'
    statement : expression_statement
    statement : compound_statement
    """
    p[0] = p[1]


def p_expression_num(p):
    """value : NUMBER"""
    p[0] = Node(NodeType.Const, p[1])


def p_expression_id(p):
    """value : ID"""
    p[0] = Node(NodeType.Var, p[1])


def p_primary_exp(p):
    """primary_expression : '(' expression ')'"""
    p[0] = p[2]


def p_unary_op(p):
    """
    unary_operator : '&'
    | '*'
    | '+'
    | '-'
    | '~'
    | '!'
    """
    p[0] = p[1]


def p_unary_exp(p):
    """unary_expression : unary_operator primary_expression"""
    p[0] = Node(NodeType.UnaryOp, p[1], p[2])


def p_exponential_exp(p):
    """exponential_expression : unary_expression POW exponential_expression"""
    p[0] = Node(NodeType.Exp, p[2], [p[1], p[3]])


def p_multiplicative_exp(p):
    """
    multiplicative_expression : multiplicative_expression '*' exponential_expression
    | multiplicative_expression '/' exponential_expression
    | multiplicative_expression '%' exponential_expression
    """
    p[0] = Node(NodeType.Mul, p[2], [p[1], p[3]])


def p_additive_exp(p):
    """
    additive_expression : additive_expression '+' multiplicative_expression
    | additive_expression '-' multiplicative_expression
    """
    p[0] = Node(NodeType.Add, p[2], [p[1], p[3]])


def p_shift_exp(p):
    """
    shift_expression : shift_expression LEFT_OP additive_expression
    | shift_expression RIGHT_OP additive_expression
    """
    p[0] = Node(NodeType.Shift, p[2], [p[1], p[3]])


def p_relational_exp(p):
    """
    relational_expression : relational_expression '<' shift_expression
    | relational_expression '>' shift_expression
    | relational_expression LE_OP shift_expression
    | relational_expression GE_OP shift_expression
    """
    p[0] = Node(NodeType.Relational, p[2], [p[1], p[3]])


def p_equality_exp(p):
    """
    equality_expression : equality_expression EQ_OP relational_expression
    | equality_expression NE_OP relational_expression
    """
    p[0] = Node(NodeType.Equality, p[2], [p[1], p[3]])


def p_assignment_op(p):
    """assignment_operator : '='"""
    # | MUL_ASSIGN
    # | DIV_ASSIGN
    # | MOD_ASSIGN
    # | ADD_ASSIGN
    # | SUB_ASSIGN
    # | LEFT_ASSIGN
    # | RIGHT_ASSIGN
    # | AND_ASSIGN
    # | XOR_ASSIGN
    # | OR_ASSIGN"""
    p[0] = p[1]


def p_assignment_exp(p):
    """assignment_expression : ID assignment_operator assignment_expression"""
    p[0] = Node(NodeType.Assign, p[2], [p[1], p[3]])


def p_if_statement(p):
    """
    statement : IF '(' expression ')' statement
    | IF '(' expression ')' statement ELSE statement
    """
    if len(p) == 6:
        p[0] = Node(NodeType.If, p[3], p[5])
    else:
        p[0] = Node(NodeType.IfElse, p[3], [p[5], p[7]])


def p_while_statement(p):
    """statement : WHILE '(' expression ')' statement"""
    p[0] = Node(NodeType.While, p[3], p[5])


def p_continue_statement(p):
    """statement : CONTINUE ';'"""
    p[0] = Node(NodeType.Continue)


def p_break_statement(p):
    """statement : BREAK ';'"""
    p[0] = Node(NodeType.Break)


def p_empty(p):
    """empty :"""
    p[0] = Node(NodeType.Empty)


def get_AST(data):
    log = logging.getLogger()

    lx = lex.lex(module=lexer)
    # lx.input(data)
    #
    # while True:
    #     tok = lx.token()
    #     if not tok:
    #         break  # No more input
    #     print(tok)

    parser = yacc.yacc(debug=1)
    result = parser.parse(data, debug=log)
    return result
