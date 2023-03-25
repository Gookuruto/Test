"""
Napisz program w Pythonie, aby sprawdzić, czy funkcja jest funkcją zdefiniowaną przez użytkownika, czy nie.
 Użyj types.FunctionType, types.LambdaType()

 hint:
 types.FunctionType
types.LambdaType
The type of user-defined functions and functions created by lambda expressions.

Raises an auditing event function.__new__ with argument code.

The audit event only occurs for direct instantiation of function objects, and is not raised for normal compilation.
"""

import types


def func():
    return 1


# przykładowa funkcja lambda
funkcja = lambda x: x + 1

# sprawdź czy funkcja jest zdefiniowana przez użytkownika
if isinstance(func, types.FunctionType):
    print("func jest funkcją zdefiniowaną przez użytkownika")
else:
    print("func nie jest funkcją zdefiniowaną przez użytkownika")

# sprawdź czy funkcja lambda jest zdefiniowana przez użytkownika
if isinstance(funkcja, types.LambdaType):
    print("funkcja jest funkcją zdefiniowaną przez użytkownika")
else:
    print("func nie jest funkcją zdefiniowaną przez użytkownika")

print(isinstance(func, types.FunctionType))
print(isinstance(func, types.LambdaType))
print(isinstance(lambda x: x, types.FunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance(max, types.FunctionType))
print(isinstance(max, types.LambdaType))
print(isinstance(abs, types.FunctionType))
print(isinstance(abs, types.LambdaType))

import types

# przykładowa funkcja
prt = print

print(type(funkcja))
prt("hello world")

def super(x):
    if isinstance(x, int):
        return x ** 2
    elif isinstance(x, str):
        return x[::-1]
    else:
        return x


print(super("to jest fajny tekst"))
