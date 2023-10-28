lst = [11, 100, 99, 1000, 999]

answer_1 = lst[0]
print("Zadanie 30")
print(answer_1)

#################################################

lst = [11, 100, 101, 999, 1001]
print("Zadanie 31")
print(lst[1])

################################################

answer_1 = lst[-1]
print("Zadanie 32")
print(answer_1)

###############################################

gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append("pajamas")
print("Zadanie 33")
print(gift_list)

################################################
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append(["socks", "tshirt", "pajamas"])
print("Zadanie 34")
print(gift_list)

###############################################
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.insert(2, 'slippers')
print("Zadanie 35")
print(gift_list)

##############################################
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer_1 = lst.index(8679)
print("Zadanie 36")
print(answer_1)
##############################################
print("Zadanie 37")
lst.remove(lst[-1])
print(lst)

##############################################
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
print("Zadanie 38")
lst.reverse()
print(lst)

###############################################
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
print("Zadanie 39")
answer_1 = lst.count(6)
print(answer_1)
###############################################
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
print("Zadanie 40")
answer_1 = sum(lst)
print(answer_1)

###############################################
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
print("Zadanie 41")
print("a")
answer_1 = min(lst)
print(answer_1)
print("b")
answer_1 = max(lst)
print(answer_1)

##################################################
print("Zadanie 43")
dict = {"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates",
        "student": "Aristotle"}
print("a")
answer_1 = dict["born"]
print(answer_1)
print("b")
# TODO napisz kod do zadania 43 b
dict["born"] = -428
print(dict["born"])

######################################################
print("Zadanie 44")
dict = {"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates",
        "student": "Aristotle"}
# TODO napisz kod do zadania 44
dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(dict)

######################################################
print("Zadanie 45")
dict = {"son’s name": "Lucas", "son’s eyes": "green", "son’s height": 32, "son’s weight": 25}
# TODO dodaj 2 do wartości son's height
dict["son’s height"] += 2

print(dict)

#####################################################
print("Zadanie 46")
dict = {"son’s name": "Lucas", "son’s eyes": "green", "son’s height": 32, "son’s weight": 25}
answer_1 = list(dict.items())

print(answer_1)

######################################################
print("zadanie 47")
dict = {"son’s name": "Lucas", "son’s eyes": "green", "son’s height": 32, "son’s weight": 25}

print("a")
print(dict.get("son’s eyes", "no key"))  # TODO wypisz wartośc klucza son's eyes

print("b")
answer_1 = dict.get("son's age",
                    "2")  # TODO Spróbuj odczytać wartośc dla klucza "son’s age"a jeżeli klucz nie istnieje zwróć wartość "2"
print(answer_1)

#############################################################
print("zadanie 48")

dict = {"son’s name": "Lucas", "son’s eyes": "green", "son’s height": 32, "son’s weight": 25}
# TODO clear dict
dict.clear()
print(dict)

#############################################################
print("Zadanie 49")
dict = {"son’s name": "Lucas", "son’s eyes": "green", "son’s height": 32, "son’s weight": 25}
answer_1 = len(dict)  # TODO Za pomocą funkcji len() sprawdź ile kluczy znajduje sie w słowniku
print(answer_1)
