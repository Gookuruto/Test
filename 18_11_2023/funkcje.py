from typing import Optional


def print_hello_world():
    print("Witaj swiecie funkcji.")


def print_hello_parameters(name):
    print(f"Witaj swiecie {name}.")


def kwadrat(number):
    z = number ** 2
    return number ** 2


def sqrt_custom(number):
    return number ** (1 / 2)


# print("Przed funckja")
# print_hello_world()
# hello_result = print_hello_parameters()
# result = kwadrat(10)
# pierwiek = sqrt_custom(100)
# if pierwiek == 10:
#     print("Success")
# print(result)
# print("Po funckja")

# def print_full_name(name: str, surname: str, title: Optional[str] = None) -> None:
#     if title is None:
#         print(f"{name} {surname}")
#     else:
#         print(f"{title} {name} {surname}")
#
#
# print_full_name("Jon", "Snow")
#
# print_full_name(surname="Jon", name="Snow")
#
# print_full_name("Jon", surname="Snow")
#
# print_full_name("Jon", "Snow", "Mr.")
#
# print_full_name("Jon", "Snow", title="Mr.")

# Argsy

def add(a, b, *args):
    print(args)
    result = a + b + sum(args)
    return result


def add_ingerdients(**kwargs):
    print(kwargs)
    if "marchewka" in kwargs:
        print("Robimy marchewkową")
    return sum(kwargs.values())


print(add_ingerdients(banan=15, ziemniaki=2, cebula=3))


def add_cos(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)  # moze byc pusta krotka
    print(kwargs)  # moze byc pusty slownik


add_cos(1, 2, 1, 1, 2, 5, 6, pope="Janek", jacek="jacu")
# print(add(1, 10))
