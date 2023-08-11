

def collapse(value):
    res = 0
    for key, val in value.items():
        res += val
    return res


def unary_op(op, value):
    res = {}
    for key, val in value.items():
        match op:
            case '-':
                res[key] = -val

    return res


def exp(val1, val2):
    val2 = collapse(val2)
    res = {}
    for key, val in val1.items():
        res[key] = val ** val2
    return res


def mul(val1, val2, op):
    val2 = collapse(val2)
    res = {}
    for key, val in val1.items():
        match op:
            case '*':
                res[key] = val * val2
            case '/':
                res[key] = val // val2
            case '%':
                res[key] = val % val2
    return res


def add(val1, val2, op):
    res = val1.copy()
    for key, val in val2.items():
        match op:
            case '+':
                if res.get(key) is None:
                    res[key] = val
                else:
                    res[key] = res[key] + val
            case '-':
                if res.get(key) is None:
                    res[key] = -val
                else:
                    res[key] = res[key] - val
    return res
