"""
Npisz program ktory wypisze pierwszy i ostatni element z listy test_list.
"""
from typing import List

test_list = ["R2D2", "Lord Vader", "Luke", "Yoda", "Han Solo"]

czesc_listy = test_list[:3]
middle = len(test_list) // 2
if len(test_list) % 2 == 0:
    lista_2 = test_list[middle - 1:middle + 1]
else:
    lista_2 = test_list[middle:middle+1]
print(lista_2)
print(test_list[4:1:-1])

# class Figura:
#     def __init__(self):
#         pass
#
#     def pole_powierzchni(self):
#         raise NotImplementedError()
#
#
# #
# #
# class Trojkat(Figura):
#     def __init__(self, h, a):
#         super().__init__()
#         self.h = h
#         self.a = a
#
#     def pole_powierzchni(self):
#         return f"Trojkat ma pole: {(self.a * self.h) / 2}"
#
#
# class Kwadrat(Figura):
#     def __init__(self, a):
#         super().__init__()
#         self.a = a
#         self.c = None
#
#     def pole_powierzchni(self):
#         return f"Kwadrat ma pole: {self.a * self.a}"
#
#
# class Kolo(Figura):
#     def __init__(self, r):
#         super().__init__()
#         self.r = r
#         self.c = None
#
#     # def pole_powierzchni(self):
#     #     return f"Kolo ma pole: {3.14 * self.r ** 2}"
#
#
# def get_figure_list() -> List[Figura]:
#     return [Kwadrat(1), Trojkat(2, 2), Trojkat(3, 3), Kolo(5)]
#
#
# # lista_figur = get_figure_list()
# #
# # for figura in lista_figur:
# #     print(figura.pole_powierzchni())
#
# pojazdy = ["Motor", "Samochod"]
# color = ["czerwony", "zielony"]
# wheels = [1, 2, 3, 4]
#
# output = [f"{vehicle} {kolor} {wheel}" for vehicle in pojazdy for kolor in color for wheel in wheels]
#
# print(output)
#
# if "Motor" in pojazdy:
#     if "niebieski" in color:
#         print("moge zrobic niebieski motor")
#     elif "czerwony" in color:
#         print("moge zrobic czerwony motor")
#     else:
#         print("Nie pokoloruje motoru.")
# else:
#     print("nie ma motoru")
#
#
# # output_2 = []
# # for vehicle in pojazdy:
# #     for kolor in color:
# #         for wheel in wheels:
# #             colored_vehicle = f"{vehicle} {kolor} {wheel}"
# #             output_2.append(colored_vehicle)
# #
# # print(output_2)
