######### czym jest zmienna, czym są typy, określanie typów w Pythonie i jak owe określanie ma się do definicji języka silnie i słabo typowanego
# zmiennia
import math

nowa_zmienna = 3.14
constant_position_offset = 5
y = 20
z = 30
# typy
"""
str 'napis'
int 5
float 5.5, -5.5
boolean True, False
complex 5+5i
NoneType: None
list []
tuple (1,2,3)
dict {key: value}, {}
set set(), {value, value2,value3} 
"""


# Operatory arytmetyczne(matematyczne)

# number = 5
# number2 = 10.0
#
# result = number + number2
# print(result)
# result = number - number2
# print(result)
# result = number * number2
# print(result)
# result = number / number2
# print(result)
# result = number // number2
# print(result)
# result = number ** number2
# print(result)
# result = number % number2
# print(result)

# napis = "Hello "
# napis2 = "world"
#
# result = napis + napis2
# print(result)
# result = napis * 5
# print(result)

# lista = ["a"]
# lista2 = [1,"a"]
#
# result = lista + lista2
# print(result)
# result = lista2*5
# print(result)

# Wyjątki
# try:
#  raise ValueError()
# except TypeError as e:
#     print(f"Wystąpił wyjątek {e}")
# finally:
#     print("Zawsze sie wykonam.")
#
# print("Program działa dalej")
#
# def wypisz(i):
#     print(i)
#
#
# for i in range(0, 10):
#     if i == 5:
#         continue
#     wypisz(i)

# comprechension
#
# lista = [i for i in range(100)]
# lista2 = [item ** 2
#           for item in lista
#           ]
# print(lista)
# print(lista2)
#
# dict_comp = {key: lista2[index] for index, key in enumerate(lista)}
# print(dict_comp)
#
# set_comp = {value for value in lista2 if value > 6000}
# print(set_comp)

# instryukcje warunkowe
# lista = ["Ania", "Jacek", "Mateusz", "Sebastian", "Ewa"]
#
# if not ("Ania" in "aniamakota" or "sebastian" in lista):
#     print("cos robimy")

# #Ciecie
# lista = [1,2,3,4,5,6,7,8]
#
# result = lista[0:3]
# print(result)
# result = lista[::2]
# print(result)
# result = lista[::-1]
# print(result)

# args kwargs

# def funckja(*args, param=None, **kwargs):
#     print(args)
#     for item in args:
#         print(item)
#     print(kwargs)
#     for key, item in kwargs.items():
#         print(key, item)
#     print(param)
#
#
# funckja(1, 2, 5, 6, 7, "hello", x=5, alicja="W krainie czarów")

# argumenty do programu

# import sys
#
# for item in sys.argv:
#     if item == "hello":
#         print("Mam argument hello")

# importowanie

# import random
# import random as rd
# from random import randint
# from random import *
#
# randint(0,100)
# rd.randint(0,100)

# iterowanie
#
# kolekcja = {1: "1", 2: "abc"}
# for item in kolekcja.items():
#     print(item)
#
# while 1 in kolekcja:
#     print("Cos robimy")
#
#     x = input("Wpisz 10 aby zakonczyc")
#     if x == "10":
#         del kolekcja[1]
#
# print(kolekcja)

# Pisanie do pliku

# with open("F:\\Python_projects\\sda\\Zadania_podstawy\\zmienne/text.txt", 'w') as f:
#     f.write("Nowy tekst 3")

# with open("F:\\Python_projects\\sda\\Zadania_podstawy\\zmienne/text.txt", 'a') as f:
#      f.write("Nowy tekst 4\n")

# Czytania z pliku

# with open("F:\\Python_projects\\sda\\Zadania_podstawy\\zmienne/text.txt", 'r') as f:
#     #print(f.read()) #Czyta caly plik
#     # for line in f:
#     #     print(line) #czyta po linijce
#
#     lines = f.readlines() #czyta wszystkie linie do listy
#     print(lines)

# Formatowanie stringów
# x = 50
# result = f"Mamy fajną liczbe {x}"
# print(result)
# result = "Mamy fajną liczbe {}".format(x)
# print(result)

# kalsy i obiekty

class Human:
    def __init__(self, height: float, weight: float, skin_color: str = None):
        self.height = height
        self.weight = weight
        self.skin_color = skin_color

    def walk(self, meters: int):
        print(f"Człowiek idzie {meters} metrów")
        return meters

    def sleep(self):
        print("człowiek śpi.")


human_instance = Human(180, 80, "violet")


# human_instance.walk(100)
# human_instance.sleep()


class Woman(Human):
    def __init__(self, height: float, weight: float, hair_length: float, partner: Human = None, skin_color: str = None):
        super().__init__(height, weight, skin_color)
        self.hair_length = hair_length
        self.partner = partner

    def cut_hair(self, cut_lenght: float):
        self.hair_length = cut_lenght
        print("Byłam u fryzjera")

    def woman_walk(self):
        print("Kobieta idzie")

    def order_man_to_shave(self, man):
        print("Idz sie ogol.")
        man.shave()

    def change_partner(self, partner: Human):
        self.partner = partner


class Man(Human):
    def __init__(self, height: float, weight: float, beard: bool, partner: Human = None, skin_color: str = None):
        super().__init__(height, weight, skin_color)
        self.beard = beard
        self.partner = partner

    def shave(self):
        self.beard = False
        print("Ogoliłem się.")

    def walk(self, meters: int):
        result = super().walk(meters)
        print("Fajnie sie chodzi")
        print(result)

    def suggest_hair_cut(self, woman, length):
        print(f"ładnie by ci było w włosach o długości {length} cm")
        woman.cut_hair(length)

    def change_partner(self, partner: Human):
        self.partner = partner

    def __str__(self):
        return f"Mezczyzna wysokośc {self.height}, waga {self.weight}"


#
# woman_instance = Woman(165, 50, 30)
# man_instance = Man(120, 100, True)
#
# man_instance.walk(10)
# woman_instance.woman_walk()

# man_instance.shave()
# print(man_instance.beard)
# woman_instance.cut_hair(100)
# print(woman_instance.hair_length)

# interakcje miedzy obiektami


woman_instance = Woman(165, 50, 30)
man_instance = Man(120, 100, True)

# woman_instance.order_man_to_shave(man_instance)
# print(man_instance.beard)
# man_instance.suggest_hair_cut(woman_instance, 45)
# print(woman_instance.hair_length)

#
# print(woman_instance.partner)
# woman_instance.change_partner(man_instance)
# print(woman_instance.partner)
# print(man_instance.partner)


# wielo dziedziczenie

# class IDontKnowWhoIAm(Man, Woman):
#     def __init__(self, height: float, weight: float, beard: bool, hair_lenght: float, skin_color: str = None):
#         super().__init__(height, weight, beard, skin_color)
#         Woman.__init__(self, height, weight, hair_lenght,skin_color=skin_color)
#
#
#
# instance = IDontKnowWhoIAm(150,100,True,100)
#
# instance.shave()
# print(instance.hair_length)
# instance.cut_hair(50)
# print(instance.hair_length)
# instance.order_man_to_shave(instance)
# print(man_instance.beard)
# instance.suggest_hair_cut(instance,200)
# print(instance.hair_length)

# sort i sorted


# lista = ["b", "a", "c"]
# lista_numery = [2, 3, 1, 4, 9, 7, 2,11]
# # lista.sort()
# posortowana_lista = sorted(lista_numery, reverse=True)
# print(lista_numery)
# print(posortowana_lista)

#metody napisów(string)

napis = "Ala ma kotaß."

print(napis.startswith('A'))
print(napis.endswith("kota"))
print(napis.lower())
print(napis.upper())
print(napis.replace(' ', '_'))
print(napis.title())
print(napis.casefold())
print(napis.split())
lista = ["Ala", "kota", "ma"]
print(",".join(lista))
napis2 = "                 Ala                  "
print(napis2.strip())
print(napis2)
print(napis)
