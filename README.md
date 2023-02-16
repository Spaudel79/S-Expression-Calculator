# S-Expression-Calculator

This is a command line program that acts as a simple calculator which takes a single argument as an expression and prints out the integer result of evaluating it.

Assuming the program is implemented in Python, invocations should look like:

$ ./calc.py 123
123

$ ./calc.py "(add 12 12)"
24

It is written in python 3.9

# Expression syntax

Since the expression is passed in as a command line argument, it is a string. The syntax resembles S-expressions but the rules are simplified. An expression can be in one of two forms:

# Integers

An integer is just a sequence of base 10 digits. For example:

 ``` 123  ``` 
 
# Function calls

A function call takes the following form:

```(FUNCTION EXPR EXPR)```

A function call is always delimited by parenthesis ( and ).

The ```FUNCTION``` is one of add or multiply.

The EXPR can be any arbitrary expression, i.e. it can be further function calls or integer expressions.

Exactly one space is used to separate each term.

For example:
```
(add 123 456)

(multiply (add 1 2) 3)
```

# Installed package

Pre commit is installed in the virtual environement for improvement of the quality of commits. 
It can be installed by following.

# Using pip:

```pip install pre-commit```
Also ```.pre-commit-config.yaml``` is added for the configuration

Moreover ```.gitignore``` file is added to remove ```.idea``` and its files

# Assumptions

A list of assumptions that were made:

1. There is no need for dealing with negative numbers.
2.Parenthesis will always be balanced.
3.Only the add and multiply functions will be called.
4.There will always be a single space between the function arguments.
5. For error handling, throwing exceptions are done when in an invalid state.  

# Validation and Error Handling

Many functions are written for the validation of the input and the error handlings which gives user a message as what type of error in expression they are giving in
the input.
Some of them are following.

1. Invalid operators except add and multiply
2. Check spacing after every operator tokens.
3. Find missing opening and or closing parentheses
4. Find missing second arguments or expression for the operation to perform.

# Improvements and Scope

1. Another operation can be added to the calculate function by adding the functionality in the function and can be run.
2. Scope of adding more than two expression in the input.


