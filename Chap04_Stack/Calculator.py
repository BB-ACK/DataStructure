from EvaluatePostfix import evalPostfix
from InfixToPostfix import infixToPostfix

infix = input("Enter... ")
expr = infix.split()

print(infix, "=", evalPostfix(infixToPostfix(expr)))