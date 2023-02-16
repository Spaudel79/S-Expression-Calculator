import re

def check_before_parsing(inputs):

    if not inputs:
        print("Empty string")
        return False

    if len(inputs) < 4:
        print("Invalid input")
        return False

    if inputs[0] != '(' or inputs[-1] != ')':
        print("Invalid parentheses")
        return False

    empty_paren_regex = r'\(\s*\)'

    if re.search(empty_paren_regex, inputs):
        print("Invalid expression: empty parentheses found")
        return False

    return True


def validate_spacing(expression):

    # Validate spacing for each function name
    for func in ["add", "multiply"]:
        func_len = len(func)
        i = 0

        if expression[i + 1:i + 1 + func_len] == func:

            # Check for correct spacing after function name
            if i + 1 + func_len < len(expression) and expression[i + 1 + func_len] != ' ':
                print("missing space after add function")
                return False

        if expression[expression.find('m'): expression.find('m') + func_len] == func:

            if expression.find('m') + func_len < len(expression) and expression[expression.find('m') + func_len] != ' ':
                print("missing space after multiply function")
                return False
    return True


def validate_parenthesis(expr_list):

    count = 0
    for char in expr_list:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
            if count < 0:
                return False

    if count != 0:
        print("missing opening or closed parantheses")
        return False
    return True