def calculate(expr):

    if isinstance(expr, int):
        return expr
    elif expr[0] == 'add':
        return calculate(expr[1]) + calculate(expr[2])
    elif expr[0] == 'multiply':
        return calculate(expr[1]) * calculate(expr[2])
    else:
        raise ValueError("Unknown operator: %s" % expr[0])






