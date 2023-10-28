# lst_1 = [1, 2, 3, 1, 3, 3, 1, 2]
# lst_2 = [1, 2, 3]
#
# lst_3 = lst_1.copy()
# for i in lst_1:
#     print(i)
#     lst_3.append(i)
#
# print(lst_3)
# print(lst_2)
# import time
#
# num = 0
# time_out = time.time() + 60
# while True:
#     num += 1
#     if num == 7:
#         continue
#     while num < 3:
#         if num == 2:
#             break
#         num += 1
#
#     print(num)
#
# print("Petla skonczona!")
import time
from typing import List, Callable


def function():
    start = time.time()
    lst = [x for x in range(10) for x in range(1000000)]
    stop = time.time()
    print(stop - start)
    lst_2 = []
    print("Normal for")
    start = time.time()
    for x in range(10):
        for x in range(1000000):
            lst_2.append(x)
    stop = time.time()
    print(stop - start)

def kwadrat(x: float) -> float:
    return x**2

def create_custom_list(lst: List[float], f:Callable) -> List[float]:
    lst_2 = []
    for item in lst:
        lst_2.append(f(item))
    return lst_2



# def robienie_ciasta(składniki: List) -> Ciasto:
#     <kroki wykonywania ciasta>
#     return Ciasto

result = create_custom_list([1,10,2,5],kwadrat)
print(result)