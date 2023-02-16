import sys
from convert import *
from calc import calculate
from validation import check_before_parsing, validate_parenthesis, validate_spacing


def main():

    user_input = sys.argv

    if len(user_input) < 2:
        print("No expression in input!")
        return

    if user_input[1].isdigit():
        result = user_input[1]
        print(result)
        return

    if not check_before_parsing(user_input[1]):
        return

    if not validate_spacing(user_input[1]):
        return

    if not validate_parenthesis(user_input[1]):
        return

    expr = ParseExpression(sys.argv[1]).convert()

    print("The output is:", calculate(expr))


if __name__ == "__main__":
    main()
