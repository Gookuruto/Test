"""
-Napisz program, który przyjmie od użytkownika wartość 3 liczb całkowitych, następnie sprawdzi,
 czy jeśli będą to długości boków, czy można z nich utworzyć trójkąt. Stosowny komunikat wypisz na ekran.
-Napisz program, który przyjmie od użytkownika nazwę aktualnego miesiąca, następnie wypisze na ekran, jaką mamy porę roku.
-Napisz program który sprawdzi czy podana przez użytkownika liczba jest podzielna przez 2.
-Napisz program który sprawdzi czy podana przez użytkownika liczba jest podzielna przez druga liczbe podana przez użytkownika.
"""

# Zadanie 55


def zadanie_55():
    name = input("Podaj liczbe: ")
    if name.lower() == "bond":
        print("Welcome on board 007.")
    else:
        print(f"Good morning {name}")


# n = 0
#
# while n<5:
#     n += 1
#     if n ==3:
#         continue
#     print(n)
# print("Koniec petli.")


# print(sum(list(range(0,101))))

# counter = 0
# total = 0
#
# while counter <= 100:
#     total += counter
#     counter += 1
#
# print("Wynik: ", total)
#
# lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
#
# my_message = ""
#
# index = 0
#
# while index < len(lst):
#     if lst[index] == 100:
#         my_message = f"There is a 100 at index no: {index}"
#     index += 1
#
# print(my_message)
#
# lst1 = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
# index = 0
# lst2 = []
# while index < len(lst1):
#     if lst1[index]:
#         lst2.append(lst1[index])
#     index += 1
#
# print(lst2)
#
# lst = [" koala ", " cat ", " fox ", " panda ", " chipmunk ", " sloth ", " penguin ", " dolphin "]
# for animal in lst:
#     print(animal)
#
# st =[ "Sam" , "Lisa" , "Micha" , "Dave" , "Wyatt" , "Emma" , "Sage" ]
#
# print(f"Hello!, {', '.join(st)}")
# for name in st:
#     print(f"Hello!, {name}")

st = ["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]


# x = 10
# while x>0:
#     x-=1
#     if x == 9:
#         continue
#     print("cos pomiedzy")
#     if x == 7:
#         continue
#     if x == 5:
#         break
#     print(x)
#
# print(f"Petla sie zakonczyła x = {x}")
#
def list_examples():
    fruits = ["apple", "banana", "lemon"]
    fruits_dict = {"apple": "", "banana": "", "lemon": ""}
    products = ["apple pie", "choco banana", "lemonade"]

    indexes = []
    for i in range(0, len(fruits)):
        indexes.append((i, fruits[i]))

    print(indexes)

    for index, fruit in enumerate(fruits):
        print(index)
        print(f"I'm making {products[index]} from {fruit}")


def odejmowanie(a: int, b: int = 0, c=0, d=0) -> int:
    return a - b - d


def add(a: int, b: int, *numbers, **kwargs):
    print(numbers)
    print(kwargs)
    result = a + b
    for argument in numbers:
        if isinstance(argument, str):
            continue
        result += argument
    for key in kwargs:
        if key == "agent_007":
            print(kwargs[key])
    return result


print(add(1, 50, "Imie", 4, 5, 6, 7.6, agent_007="James Bond"))
