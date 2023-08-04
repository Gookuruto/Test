# Z68
lst1 = [1, 2, 3, 4, 5]
lst2 = [i for i in lst1]
print(lst2)

# Z69
lst = [i for i in range(1200, 2000, 130)]
print(lst)

# Z70
lst1 = [44, 54, 64, 74, 104]
lst2 = [i + 6 for i in lst1]
print(lst2)

# Z71
lst1 = [2, 4, 6, 8, 10, 12, 14]
lst2 = [i ** 2 for i in lst1 if i ** 2 > 50]

print(lst2)

# 72
dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
        "Motorcycle": 110}

lst = [name.upper() for name in dict if dict[name] < 5000]

print(lst)
