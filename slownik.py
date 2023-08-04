# z43
dict = {"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates",
        "student": "Aristotle"}

answer = dict["born"]

print(answer)

dict["born"] = -428

print(dict)

#z44
dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]

print(dict)

#z45

dict = {" son ’s name ": " Lucas ", " son ’s eyes ": " green ", "son’s height": 32, " son ’s weight ": 25}
dict["son’s height"] += 2

print(dict["son’s height"])

#Z46
print(list(dict.items()))
#z47


print(dict.get(" son ’s eyes "))
print(dict.get("son's age","2"))

#z48

dict2 = dict.copy()
print(dict2)
dict2.clear()
print(dict2)
#49
print(len(dict))


