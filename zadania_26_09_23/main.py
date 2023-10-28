# print("zadanie 58")
# lst = [10, 99, 98, 85, 45, 100,59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
# my_message = "There is a 100 at index no:"
#
# c = 0
# while c < len(lst):
#     if lst[c] == 100:
#         my_message += f" {c}, "
#     c+=1
#
# print(my_message)
# print("zadanie 59")
# lst1 =[ "Joe" , "Sarah" , "Mike" , "Jess" , "" , "Matt" , "" , "Greg" ]
#
# def name_adder(l):
#     lst = []
#     index = 0
#     while index < len(l):
#         if l[index]:
#             lst.append(l[index])
#         index +=1
#     return lst
#
# print(name_adder(lst1))

# lst = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
# print(", ".join(lst))
# for animal in lst:
#      print(animal, end=', ')
# print("Zadanie 61")
# lst = ["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
# for name in lst:
#     print("Hello!,", name)
#
# for name in lst:
#     print(f"Hello!,{name}")
# print("Zadanie 62")
# str = "Civilization"
# c=0
# for i in str:
#     print(i)
#     c +=1
# print(c)

print("Zadanie 66")
dict = {"z1": 900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
dict_list = [900, 1100, 2300, 1050, 3200, 400]
lst = []
for key in dict:
    if dict[key] > 1000:
        lst.append(dict[key] - 1000)
for value in dict.values():
    if value > 1000:
        lst.append(value - 1000)
dict_list = [("z1", 900), ("t1", 1100)]
for key, value in dict.items():
    if dict[key] > 1000:
        lst.append(value - 1000)
print(lst)
