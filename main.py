import sys
from convert import *
from calc import *
from validation import *

def main():

    user_input = sys.argv

    if len(user_input) < 2:
        print('No expression in input!')
        return

    if user_input[1].isdigit():
        return user_input[1]

    if not check_before_parsing(user_input[1]):
        return

    expr = ParseExpression(sys.argv[1]).convert()

    if not validate(expr):
        return

    print("The output is:",calculate(expr))


if __name__ == '__main__':
    main()
