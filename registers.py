from values import Var


def __create_reg__(addr):
    return Var('absolute', addr, '/reg')


mul = __create_reg__(-1)
div = __create_reg__(-2)
unary_minus = __create_reg__(-4)
mod = __create_reg__(-5)
exp = __create_reg__(-6)
l_shift = __create_reg__(-7)
r_shift = __create_reg__(-8)
b_and = __create_reg__(-9)
b_or = __create_reg__(-10)
b_xor = __create_reg__(-11)
conv = __create_reg__(-12)
eq = __create_reg__(-13)
neq = __create_reg__(-14)
less_than = __create_reg__(-15)
less_eq = __create_reg__(-16)
gr_than = __create_reg__(-17)
gr_eq = __create_reg__(-18)


stack_ptr = __create_reg__(-101)
stack_shift = __create_reg__(-102)
ptr = __create_reg__(-103)
ptr_shift = __create_reg__(-104)


jump = __create_reg__(-200)


ptr_reg_num = {
    stack_ptr: 1,
    stack_shift: 2,
    ptr: 3,
    ptr_shift: 4
}



