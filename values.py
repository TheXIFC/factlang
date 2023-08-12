import static_calc


class Var:
    is_var = True
    is_const = False

    def __init__(self, scope, addr, name='/'):
        self.scope = scope
        self.addr = addr
        self.name = name
        self.is_temp = (name == '/temp')


class Const(dict):
    is_var = False
    is_const = True

    def __init__(self, type, value):
        self[type] = value

    def to_int(self):
        return static_calc.collapse(self)


class Pointer:
    def __init__(self, origin, shift_var: Var = None):
        self.const = False
        self.origin = None
        self.shift_const = 0
        self.shift_var = shift_var
        self.reg = None

        if isinstance(origin, Var):
            self.origin = origin
        elif isinstance(origin, Const):
            self.add_shift(origin)
            self.const = True

    def add_shift(self, shift):
        if isinstance(shift, Var):
            if self.shift_var is not None:
                raise Exception("Shift var was already set")
            self.shift_var = shift
        elif isinstance(shift, Const):
            self.shift_const += shift.to_int()
        else:
            self.shift_const += shift

