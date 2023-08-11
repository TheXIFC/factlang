from values import Var


class SubScope:

    def __init__(self):
        self.variables = {}
        self.stack = []
        self.free_space = []

    def get_var_from_scope(self, name):
        if (addr := self.variables.get(name)) is not None:
            return addr
        return None

    def add_var_to_scope(self, name='/'):
        if len(self.free_space) > 0:
            address = self.free_space.pop(0)
            self.stack[address] = name
        else:
            address = len(self.stack)
            self.stack.append(name)

        if not name.startswith('/'):
            self.variables[name] = address

        return address

    def remove_at(self, i: int):
        name = self.stack[i]
        if not name.startswith('/'):
            del self.variables[name]
        self.stack[i] = None
        self.free_space.append(i)

    def copy(self):
        sub_sc = SubScope()
        sub_sc.variables = self.variables.copy()
        sub_sc.stack = self.stack.copy()
        sub_sc.free_space = self.free_space.copy()
        return sub_sc


class Scope:

    def __init__(self):
        self.gs = SubScope()
        self.ls = SubScope()

    def get(self, scope):
        if scope == 'gs':
            return self.gs
        elif scope == 'ls':
            return self.ls
        raise Exception("Unknown scope")

    def get_var(self, name, create=''):
        # if ls is not None and (addr := ls.get_var_from_scope(id)) is not None:
        if (addr := self.ls.get_var_from_scope(name)) is not None:
            return Var('local', addr, name)
        if (addr := self.gs.get_var_from_scope(name)) is not None:
            return Var('global', addr, name)

        if create == '':
            return None

        if create == 'ls':
            addr = self.ls.add_var_to_scope(name)
            return Var('local', addr, name)

        if create == 'gs':
            addr = self.gs.add_var_to_scope(name)
            return Var('global', addr, name)

        raise Exception("Unknown scope")

    def alloc_temp(self, node):
        name = '/temp'
        addr = self.ls.add_var_to_scope(name)
        var = Var('local', addr, name)
        node.temp_vars.append(var)
        return var

    def remove_temp(self, var):
        if var.scope != 'local':
            raise "Removal of non-local variable"

        self.ls.remove_at(var.addr)

    def copy(self):
        sc = Scope()
        sc.gs = self.gs
        sc.ls = self.ls.copy()
        return sc




