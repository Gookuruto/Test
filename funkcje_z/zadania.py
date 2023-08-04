"""
- Napisz funkcje_z która przyjmie liczbę całkowitą n i zwróci liste z n pierwszymi elementami ciągu fibonacciego
 def fib(n:int) -> List[int]:
    https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
- napisz funkcje_z która zsumuje wszystkie elementy w liście.
    def sum_list(lista) -> float:
        return suma
- Napisz funkcje_z która znajdzie największą z 3 liczb
    def max_of_three(x,y,z) -> int:
        return x lub y lub z

- Pomyśł jakie inne funkcje_z moga być użyteczne?

"""
from typing import List


def compare(x: int, y: int, z: int) -> int:
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z
    else:
        return 0


def compare_2(x, y, z) -> int:
    return max([x, y, z])


def sum_list(numbers: List[float]) -> float:
    return sum(numbers)


def sum_list_2(numbers: List[float]) -> float:
    result = 0
    for number in numbers:
        result += number
    return result


def fib_one_number(n: int) -> int:
    if n in [0, 1]:
        return n
    return fib_one_number(n - 1) + fib_one_number(n - 2)

def fib_one_number_1(n):
    prev = 0
    prev_2 = 0
    current_item = 0
    if n in [0, 1]:
        return n
    for item in range(n+1):
        if item == 1:
            current_item = 1
            prev = 1
        else:
            current_item = prev + prev_2
            prev_2 = prev
            prev = current_item
    return current_item

def fib(n: int) -> List[int]:
    return [fib_one_number_1(x) for x in range(n+1)]

print(fib(30))