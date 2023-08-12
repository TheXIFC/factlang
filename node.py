from enum import Enum
from scope import Scope


class NodeType(Enum):
    Script = "script"
    StatementList = "statement_list"
    EmptyBlock = "empty_block"
    Empty = "empty"
    Const = "const"
    Var = "var"
    UnaryOp = "unary_op"
    Exp = "exp"
    Mul = "mul"
    Add = "add"
    Assign = "assign"
    Shift = "shift"
    Relational = "relational"
    Equality = "equality"
    If = "if"
    IfElse = "if_else"
    While = "while"
    Continue = "continue"
    Break = "break"


class Node:

    def __init__(self, type: NodeType, leaf=None, children=None):
        self.const = False
        self.temp_vars = []
        self.value = None

        self.type = type
        if children:
            if isinstance(children, Node):
                self.children = [children]
            else:
                self.children = children
        else:
            self.children = []
        self.leaf = leaf

    def cleanup(self, scope: Scope):
        for var in self.temp_vars:
            scope.remove_temp(var)
        self.temp_vars = []
