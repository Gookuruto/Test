lista = ["a","b","c","d","h","a","g","l","m","c"]

lista_custom = [1, 2, '123', 1.0, '458.5', 10, 20, 30, 100, 200, 300]
print(lista)
print(lista_custom)
sorted_list = sorted(lista)

lista_custom.sort(key=float)
print(lista)
print(sorted_list)
print(lista_custom)