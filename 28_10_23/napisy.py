title = "genral"
name = "kenobi"

napis = "Hello there, %s %s" % (title, name)
napis_v2 = "Hello there, {gen} {ken}".format(gen = title, ken = name)
napis_v3 = f"Hello there, {title} {name}"
print(napis_v3)


header1 = "Name"
header2 = "Age"
name = "John"
age = 22
#
# print(f"| {header1:10} | {header2:10} |")
# print("-"*27)
# print(f"| {name:10} | {str(age):10} |")


napis = "Hello, World!"

#napis[start:end:step]
napis = napis.replace("!",".")
print(napis)
# print(napis[7:12])
# print(napis[::2])
# print(napis[-7::-1])