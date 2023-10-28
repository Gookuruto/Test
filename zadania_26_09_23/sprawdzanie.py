# def just_while_loop():
#     c = 0
#     while True:
#         c += 1
#         print(c)
#         if c == 100:
#             break
#
#
# def create_person_dictonary(name, surname, id):
#     person = {"name": name, "surname": surname, "id": id}
#     return person
#
#
# def get_list_of_positive_numbers(lst):
#     results = []
#     for item in lst:
#         if item >= 0:
#             results.append(item)
#     return results
#
#
# new_person = create_person_dictonary("Maciej", "Puchala", "Cws123")
#
# positive_list = get_list_of_positive_numbers([-1, 1, 2, 4, 5, -20, -67, 67, -12, 4])
# print(new_person)
# print(positive_list)
#

x = "Maciej"
y = "Mateusz"
print("Czesc %s co tam u %s" % (x, y))
print("Czesc {} co tam u {}".format(x, y))
print("Czesc {maciek} co tam u {mateusz}".format(maciek=x, mateusz=y))
print(f"Czesc {x} co tam u {y}")
print("Czesc " + str(x) + " co tam u " + str(y))

napis = type(x)

print(type(napis))
