"""
Utwórz listę 100 losowych liczb z zakresu <1-1000> i wykonaj poniższe zadania:
-Napisz program, który obliczy i wypisze na ekran sumę wszystkich elementów listy.
-Napisz program, który znajdzie i wypisze na ekran najmniejszy element listy (wykonaj 2 wersje, bez użycia i używając wbudowaną funkcję języka Python).
-Napisz program, który znajdzie i wypisze na ekran największy element listy (wykonaj 2 wersje, bez użycia i używając wbudowaną funkcję języka Python).
"""

import random as rnd

random_numbers = [rnd.randint(0, 1000) for i in range(100)]
maximum = 0
minimum = 99999
suma = 0

#list_rand.sort()
for number in random_numbers:
    suma += number
    if maximum < number:
        maximum = number
    if minimum > number:
        minimum = number

print("Suma")
print(suma)
print(sum(list_rand))
print("Maximum")
print(maximum)
print(max(list_rand))
print("Minimum")
print(minimum)
print(min(list_rand))
