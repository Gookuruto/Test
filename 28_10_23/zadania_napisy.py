# 16
print("Zadanie 16")
napis = "It’s always darkest before dawn."
print(napis)
# 17
print("Zadanie 17")
witaj = "Witaj "
imie = "Jozek"

print(witaj, imie, sep="")
print(witaj + imie)
print(f"{witaj}{imie}")
print("{}{}".format(witaj, imie))
print("%s%s" % (witaj, imie))
# 18
print("Zadanie 18")
ans = napis[0] + napis[1] + napis[-1]
ans_v2 = napis[0:2] + napis[-1]
print(ans)
print(ans_v2)
# 19
print("Zadanie 19")
ans = napis.replace(".", "!")
print(ans)
# 20
print("Zadanie 20")
napis ="EVERY Strike Brings Me Closer to the Next Home run ."
napis = napis.lower()

print(napis)

# 21
print("Zadanie 21")
napis =" don ’t stop me now ."

napis = napis.upper()
print(napis)
# 22
print("Zadanie 22")
napis ="There are no traffic jams along the extra mile ."
ans_1 = napis[0] == "A"
ans_1_v2 = napis.startswith("A")

print(ans_1)
print(ans_1_v2)
# 23
print("Zadanie 23")
napis = "There are no traffic jams along the extra mile."
ans_1 = napis[-1] == "."
ans_1_v2 = napis.endswith(".")

print(ans_1)
print(ans_1_v2)
# 24
print("Zadanie 24")
napis ="The best revenge is massive success."
print("a")
ans_1 = napis.index("v")
print(ans_1)
print("b")
ans_1 = napis.find("v")
print(ans_1)
print("c")
#napis.index("!")# jak nie ma znaku w napisie to wyrzuca błąd
print(napis.find("!"))# jak nie ma znaku w napisie to zwraca -1

# 25
print("Zadanie 25")
napis ="People often say that motivation doesn ’t last . Well , neither does bathing . That ’s why we recommend it daily."

ans_1 = napis.count("a")
ans_2 = napis.count("o")

print(" count of a is : " , ans_1 , " count of o is : " , ans_2 )

# 26
print("Zadanie 26")
napis ="1.975.000"
ans_1 = len(napis)
print(ans_1)
# 27
print("Zadanie 27")
wrd ="Toscana"
a_index = wrd.index("a")
ans_a = wrd[:a_index]
print(ans_a)
ans_b = wrd[3:]
print(ans_b)
ans_c = wrd[3:6]
print(ans_c)
ans_d = wrd[::2]
print(ans_d)
#len(wrd)-1
ans_e = wrd[1:6:2]
print(ans_e)
ans_f = wrd[::-1]
print(ans_f)