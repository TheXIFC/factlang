class Var:
    is_var = True
    is_const = False

    def __init__(self, scope, addr, name='/'):
        self.scope = scope
        self.addr = addr
        self.name = name


class Const(dict):
    is_var = False
    is_const = True

    def __init__(self, type, value):
        self[type] = value
