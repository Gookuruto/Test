# Zadanie 76
import copy
from typing import List, Any, Callable

print("#Zadanie 76")


def f_1():
    print("Hello world!")


f_1()
# Zadanie 77
print("#Zadanie 77")


def f_1():
    print("Hello world!")


ans_1 = f_1()
print(ans_1)

# Zadanie 78
print("#Zadanie 78")


def f_1():
    result = "Hello world!"
    return result


ans_1 = f_1()
print(ans_1)
# Zadanie 79
print("#Zadanie 79")


def f_1():
    print("Hello world!")
    return "Hello world!"


ans_1 = f_1()
print(ans_1)
# Zadanie 80
print("#Zadanie 80")


def f_1(*args):
    return 100


print(f_1(999))
print(f_1(70))
# Zadanie 81
print("#Zadanie 81")


def f_1(number: int):
    return number


print(f_1(44))
print(f_1("Maciej"))
# Zadanie 82
print("#Zadanie 82")
lst = [100, 200, 300, 400, 500]


def f_1(collection: List[Any]):
    #zmienia zroblowa liste
    # collection.reverse()
    # return collection
    #nie zmienia
    # lst2 = collection[::-1]
    # return lst2
    lst2 = reversed(collection)
    return list(lst2)

def f_2(collection: List[Any]):
    #zmienia zroblowa liste
    collection_copy = copy.deepcopy(collection)
    collection_copy.reverse()
    return collection_copy

lst2 = f_1(lst)
print(lst)
print(lst2)
lst2.append("Super")
print(lst2)
print(lst)
print(lst is lst2)

# Zadanie 83
print("#Zadanie 83")


def f_1():
    name = input("Podaj swoje imie: ")
    print(f"Hello {name}")

f_1()


# Zadanie 84
print("#Zadanie 84")


def f_1(number: int):
    return number+5


def f_2(number: int):
    return f_1(number)*2

print(f_2(6))
print(f_2(2137))

def caluclate_area(f: Callable,a:int,b:int):
    return f(a,b)

def calculate_rect_area(a,b):
    return a*b

def calulate_circle(r,*args):
    return 3.14*r*r


print(caluclate_area(calculate_rect_area,5,5))
