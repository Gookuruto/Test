"""
sprawdz w jaki sposób możesz zmieniać wartości w poniższej krotce bez ich nadpisywania. bez uzywania operatora =
"""

krotka = (1, "Hello", [1, 2, 3, 4, 5], {"Saitama": "One Punch Man", "Yoda": "Star Wars"})

krotka[2].reverse()
print(krotka)
