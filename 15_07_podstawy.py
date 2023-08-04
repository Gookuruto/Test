# Z61
# st = ["Sem", "Lise", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
#
# for name in st:
#     print("---------------Nowa iteracja-------------------")
#     print(f"Hello!, {name}")
#     print("Hello!,", name)
#     print("Hello!, {}".format(name))
#     print("Hello!, %s" % name)
#     s = "Hello!, " + str(name)
#     print(s)
#
# Z62
# str = "Civilization"
#
# c = 0
# for i in str:
#     # Type your answer here .
#     c += 1
#
# print(c)

# Z63
# lst1 = ["Phil","Oz","Seuss","Dre"]
# lst2 = []
# for name in lst1:
#     lst2.append(f"Dr. {name}")
#
# print(lst2)

# Z64
# lst1 =[3 , 7 , 6 , 8, 9, 11 , 15 , 25]
# lst2 = []
#
# for number in lst1:
#     lst2.append(number**2)
#
# print(lst2)
# Z65
# lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
# lst2 = []
# for number in lst1:
#     if number > 0:
#         lst2.append(number)
#
# print(lst2)
# Z66
dict = {"z1": 900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst = []
# 1 Opcja
# for element in dict:
#     if dict[element] > 1000:
#         lst.append(dict[element]-1000)

# 2 Opcja
# print(dict.items())
# for key, value in dict.items():
#     if value > 1000:
#         lst.append(value - 1000)

# Opcja 3
# print(dict.values())
# for value in dict.values():
#     if value > 1000:
#         lst.append(value - 1000)
#
# print(lst)

# Z67
# lst1 = [3.14, 66, "Teddy Bear", True, [], {}]
# lst2 = []
# for element in lst1:
#     lst2.append(type(element))
#
# print(lst2)


# lst1 = ["Phil", "Oz", "Seuss", "Dre", "Peter"]
#
# lst2 = [f"Dr. {name}"
#         for name in lst1
#         ]
# print(lst2)

# keys_values = [(1, "a"), (2, "b"), (3, "c")]
# slownik = {number: letter for number, letter in keys_values}
# print(slownik)
