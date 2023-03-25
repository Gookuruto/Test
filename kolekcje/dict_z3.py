"""
-Napisz program, który doda nowy element do istniejącego słownika.
-Napisz program, który połączy zawartość trzech słowników w jeden.
-Napisz program, który sprawdzi czy dany klucz występuje już w słowniku.
-Napisz program, który wygeneruje i wypisze na ekran słownik o kluczach wartości 1-n,
 gdzie n poda użytkownik. Dla każdego klucza x, wartość elementu ma wynosić x do potęgi drugiej.
"""

istniejacy_slownik = {"g": 11}
slownik_2 = {"a": 1, "b": 2}
slownik_3 = {"c": 3, "d": 4}

# print(istniejacy_slownik)
nowy_slownik = istniejacy_slownik | slownik_2 | slownik_3
nowy_slownik_2 = {}
nowy_slownik_2.update(slownik_2)
nowy_slownik_2.update(slownik_3)
# nowy_slownik_2.update(**istniejacy_slownik, **slownik_2, **slownik_3)
# print(nowy_slownik)
# print(nowy_slownik_2)

if "c" in slownik_2:
    print(slownik_2["a"])
else:
    print("nie ma klucza")

if slownik_2.get("c") is None:
    print("nie ma klucza")
else:
    print(slownik_2["a"])

try:
    print(slownik_2["a"])
except KeyError:
    print("nie ma klucza")

while True:
    n = input("Podaj liczbe elementów słownika: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Wartość nie jest numerem.")


user_dict = {x: x ** 2 for x in range(1, n)}

print(user_dict)