# 76
def f_1():
    print("Hello World!")


# 77
def f_1():
    print("Hello World!")


# ans_1 = f_1()
# print(ans_1)

# 78
def f_1():
    return "Hello World!"


# ans_1 = f_1()
# print(ans_1)

# 79
def f_1():
    print("Hello World!")
    return "Hello World!"


# ans_1 = f_1()
# print(f"Out of function: {ans_1}")

# 80
def f_1(*args):
    return 100


# print(f_1("hello"))

# 81
def f_1(number: int):
    return number


# print(f_1(999))

# 82
lst = [100, 200, 300, 400, 500]


def f_1(lst):
    return lst[::-1]


# 83
def f_1():
    name = input("Podaj swoje imie: ")
    print(f"Hello, {name}")


# 84

def f_1(number: int):
    return number + 5


def f_2(number: int):
    f_1_result = f_1(number)
    return f_1_result * 2


# print(f_2(4))

def recurence(n: int):
    if n < 2:
        return 1
    else:
        return recurence(n - 1) + recurence(n - 2)


# print(recurence(100))


def fib(n: int):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a
    yield b
for i in fib(100):
    print(i)

