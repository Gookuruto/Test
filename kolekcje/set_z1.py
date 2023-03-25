"""
Wypisz na ekran informację czy zbiór X zawiera liczbę 5.
Wypisz na ekran informację czy zbiór X jest podzbiorem zbioru Y.
Wypisz na ekran informację czy zbiór Y jest podzbiorem zbioru X.
Wypisz na ekran informację czy zbiór X jest nadzbiorem zbioru Y.
Wypisz na ekran informację czy zbiór Y jest nadzbiorem zbioru X.
Wypisz na ekran sumę zbiorów X oraz Y.
Wypisz na ekran różnicę zbiorów X oraz Y.
Wypisz na ekran różnicę zbiorów Y oraz X.
Wypisz na ekran iloczyn zbiorów X oraz Y.
Przekopiuj wszystkie elementy zbioru X do zbioru Y.
Wyczyść oba zbiory.

dla powtarzalnych wynikówmożecie zmienić zbiory na nielosowe.
"""
import random

X = {1, 2, 10}
Y = {1, 2, 3, 4, 5, 6, 8}
Z = {50, 20, "34"}

print('zbior X: ', X)
print('zbior Y: ', Y)
print(5 in X)
print(X.union(Y, Z))
print(Y.difference(X))
print(X.intersection(Z))
print(X.isdisjoint(Z))
X.clear()
print(X)
