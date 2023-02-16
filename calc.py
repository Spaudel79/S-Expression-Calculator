def calculate(expr):

    if isinstance(expr, int):
        return expr

    elif expr[0] == "add":
        try:
            return calculate(expr[1]) + calculate(expr[2])
        except:
            print("missing second argument to add")

    elif expr[0] == "multiply":
        try:
            return calculate(expr[1]) * calculate(expr[2])
        except:
            print("missing second argument to multiply")
    else:
        raise ValueError("Unknown operator: %s" % expr[0])
