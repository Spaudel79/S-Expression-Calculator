import re

class ParseExpression:

    def __init__(self, input_string=''):
        self.input_string = input_string

    def convert(self):
        s = self.input_string

        if self.input_string == '':
            return None

        stack = []
        lefts = []
        for element in re.findall(r'\w+|[()]', s):
            if element == ')':
                index = lefts.pop()
                stack[index:] = stack[index:],
            elif element == '(':
                lefts.append(len(stack))
            else:
                if element.isdigit():
                    element = int(element)
                stack.append(element)
        return stack[0]




