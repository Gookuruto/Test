print("zadanie 57")
counter = 0
total = 0
while counter <= 100:  # wykonujemy petle od 0 do 100 włącznie
    total += counter  # dodajemy kolejna liczbe do wyniku
    counter += 1  # tworzymy kolejną liczbe w kolejności

print(total)

######################################################
print("zadanie 58")
lst = [10, 99, 98, 85, 45, 100, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
my_message = "There is a 100 at index no:"

c = 0
while c < len(lst):
    if lst[c] == 100:
        my_message += f" {c}, "
    c += 1

print(my_message)

########################################################
print("zadanie 59")
lst1 = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]


def name_adder(l):
    lst = []
    index = 0
    while index < len(l):
        if l[index] != "":
            lst.append(l[index])
        index += 1
    return lst


print(name_adder(lst1))

##########################################################
print("Zadanie 60")
lst = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
print(", ".join(lst))
for animal in lst:
    print(animal, end=', ')
for animal in lst:
    print(animal)

##########################################################
print("Zadanie 61")
lst = ["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for name in lst:
    print("Hello!,", name)

for name in lst:
    print(f"Hello!,{name}")

##########################################################
print("Zadanie 62")
str = "Civilization"
c = 0
for i in str:
    c += 1
print(c)

##########################################################
print("Zadanie 63")
lst1 = ["Phil", "Oz", "Seuss", "Dre"]
lst2 = []
for person in lst1:
    # opcja 1
    lst2.append(f"Dr. {person}")
    # opcja 2
    lst2.append("Dr. " + person)
    # opcja 3
    lst2.append("Dr. {}".format(person))
    # opcja 4
    lst2.append("Dr. %s" % person)

print(lst2)

##########################################################
print("Zadanie 64")
lst1 = [3, 7, 6, 8, 9, 11, 15, 25]
lst2 = []
for number in lst1:
    lst2.append(number * number)

print(lst2)

##########################################################
print("Zadanie 65")
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []
for number in lst1:
    if number >= 0:
        lst2.append(number)

print(lst2)

##########################################################
print("Zadanie 66")
dict = {" z1 ": 900, " t1 ": 1100, " p1 ": 2300, " r1 ": 1050, " k1 ": 3200, " g1 ": 400}
lst = []
for key in dict:
    if dict[key] > 1000:
        lst.append(dict[key] - 1000)
for value in dict.values():
    if value > 1000:
        lst.append(value - 1000)
for key, value in dict.items():
    if dict[key] > 1000:
        lst.append(value - 1000)
print(lst)

##########################################################
print("Zadanie 67")
lst1 = [3.14, 66, "Teddy Bear", True, [], {}]
lst2 = []

for item in lst1:
    lst2.append(type(item))
print(lst2)
##########################################################
print("Zadanie 68")
lst1 = [1, 2, 3, 4, 5]
lst2 = [x for x in lst1]
print(lst2)

##########################################################
print("Zadanie 69")

lst = [number for number in range(1200, 2000, 130)]
print(lst)

##########################################################
print("Zadanie 70")
lst1 = [44, 54, 64, 74, 104]
lst2 = [item + 6 for item in lst1]

print(lst2)

##########################################################
print("Zadanie 71")
lst1 = [2, 4, 6, 8, 10, 12, 14]
lst2 = [item ** 2 for item in lst1 if item ** 2 > 50]

print(lst2)

##########################################################
print("Zadanie 72")
dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
        "Motorcycle": 110}
lst = [key.upper() for key, value in dict.items() if value < 5000]
print(lst)
