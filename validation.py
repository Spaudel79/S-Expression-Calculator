
def check_before_parsing(inputs):

    if not inputs:
        print("Empty string")
        # sys.exit()
        return False

    if len() < 4:
        print("Invalid input")
        return False

    if inputs[0] != '(' or inputs[-1] != ')':
        print("Invalid parenthesis")

        return False

    s = inputs
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)

        elif c == ")":
            if len(stack) == 0 or stack[-1] != "(":
                print("Invalid parenthesis placement")
                return False
            stack.pop()
    # return len(stack) == 0
    return True


def validate(expr_list):

    count = 0

    for char in expr_list:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
            if count < 0:
                return False

    if count != 0:
        return False
    return True