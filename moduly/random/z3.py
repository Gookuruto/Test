"""
Napisz program w języku Python, który utworzy listę losowych liczb całkowitych i losowo wybierze wiele elementów z tej listy.
uzyj funkcji random.sample()
https://docs.python.org/3/library/random.html?highlight=random#module-random
"""
import random


def losowa():
    numbers = [random.randint(0, 100) for _ in range(0, 100)]
    print(numbers)
    losowe_elementy = random.sample(numbers, 10)
    print(losowe_elementy)


# numbers = []
# for i in range(0, 50):
#     numbers.append(random.randint(0, 50))
#
#
#
# losowe_elementy = random.sample(numbers, 5)
#
# print('Lista losowych liczb:\n ', numbers)
#
# print('Losowe elementy z tej listy: \n', losowe_elementy)
#
# lista = [x for x in range(50)]
# print(lista)
# dowolny_ciąg = random.sample(lista,3)
# print(dowolny_ciąg)

# utwórz listę losowych liczb całkowitych z przedziału 0-500 o długości 10
list = random.sample(range(500), 10)

# losowo wybierz 3 elementy z listy
random_elements = random.sample(list, 3)

# wyświetl wynik
print("Lista losowych liczb całkowitych:", list)
print("Losowo wybrane elementy z listy:", random_elements)

lista = [random.randint(1, 1000) for x in range(50)]
print(lista)
dowolny_ciąg = random.sample(lista, 3)
print(dowolny_ciąg)
