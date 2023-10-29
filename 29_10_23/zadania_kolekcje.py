# 28
print("Zadanie 28")
ans_a = []
ans_b = {}
ans_c = ()
print(ans_a, type(ans_a))
print(ans_b, type(ans_b))
print(ans_c, type(ans_c))
# 29
print("Zadanie 29")
lst_a = [1, 2, "a"]
print(lst_a)
dict_b = {"imie": "Maciej", "wzrost": 200}
dict_b_v2 = {}
dict_b_v2["Name"] = "Hubert"
print(dict_b)
print(dict_b_v2)
krotka = (1, 2, 3)
print(krotka)
# 30
print("Zadanie 30")
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]

print(answer_1)
# 31
print("Zadanie 31")
print(lst[1])
# 32
print("Zadanie 32")
lst = [11, 100, 101, 999, 1001]
answer_1 = lst[-1]  # latwiejsza opcja
answer_1_v2 = lst[len(lst) - 1]  # kombinacje ale tez sie uda
print(answer_1)
print(answer_1_v2)

# 33
print("Zadanie 33")
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append('pajamas')

print(gift_list)

# 34
print("Zadanie 34")
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append(['socks', 'tshirt', 'pajamas'])

print(gift_list)
# 35
print("Zadanie 35")
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.insert(2, 'slippers')

print(gift_list)
# 36
print("Zadanie 36")
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer_1 = lst.index(8679)
print(answer_1)
# 37
print("Zadanie 37")
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.remove(lst[-1])  # zadziala jezeli elementy sa unikalne
# lst.pop() # zadziała zawsze!

print(lst)
# 38
print("Zadanie 38")
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.reverse()
# lst_reversed = list(reversed(lst))

print(lst)
# print(lst_reversed)

# 39
print("Zadanie 39")
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

ans = lst.count(6)

print(ans)

# 40
print("Zadanie 40")
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
ans = sum(lst)

print(ans)
# 41
print("Zadanie 41")
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
ans_a = min(lst)
ans_b = max(lst)
lst.sort()
ans_a_v2 = lst[0]
ans_b_v2 = lst[-1]
print(f"Minimum: {ans_a}, {ans_a_v2}")
print(f"Maximum: {ans_b}, {ans_b_v2}")
# 43
print("Zadanie 43")
dict = {"name": "Plato", "country": "Ancient Greece", "born": -427,
        "teacher": "Socrates",
        "student": "Aristotle"}
ans_a = dict["born"]
print(f"Palto urodził sie w roku: {ans_a}")
dict["born"] = -428
print(f'Palto urodził sie w roku: {dict["born"]}')

# 44
print("Zadanie 44")
dict = {"name": "Plato", "country": "Ancient Greece", "born": -427,
        "teacher": "Socrates",
        "student": "Aristotle"}
dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]

print(dict)
# 45
print("Zadanie 45")
dict = {"son's name": "Lucas",
        "son's eyes": "green",
        "son's height": 32,
        "son's weight": 25}
dict["son's height"] += 2
print(dict)
print(dict["son's height"])

# 46
print("Zadanie 46")
dict = {"son's name": "Lucas",
        "son's eyes": "green",
        "son's height": 32,
        "son's weight": 25}
ans = list(dict.items())

print(ans, type(ans))
# 47
print("Zadanie 47")
dict = {"son's name": "Lucas",
        "son's eyes": "green",
        "son's height": 32,
        "son's weight": 25}
print(dict.get("son's eyes"))
print(dict.get("son's age", "2"))
# 48
print("Zadanie 48")
dict = {"son's name": "Lucas",
        "son's eyes": "green",
        "son's height": 32,
        "son's weight": 25}
dict.clear()
print(dict)
# 49
print("Zadanie 49")
dict = {"son's name": "Lucas",
        "son's eyes": "green",
        "son's height": 32,
        "son's weight": 25}
ans = len(dict)
print(ans)
