"""
Napisz prosty program ktory wygeneruje
losowy kolor:heksadecymalny,
losoowy ciag alfabetyczny znaków,
losowa liczbe z danego przedziału
losową wielokrotność liczby 7 z zakresu 0-70.
 uzyj random.randint(), random.choice(),
  do losowej litery moZna tez uzyc modulu string
"""
import random
import string

print("Lsosowy kolor hexadecymalny: ")
print("#{:06x}".format(random.randint(0, 0xFFFFFF)))
print("Losowy ciag alfabetyczny:")
max_lenght = 255
s = ""
for i in range(random.randint(1, max_lenght)):
    s += random.choice(string.ascii_letters)
print(s)
# list_of_letters = []
# for i in range(0, max_lenght):
#     letter = (random.choice(string.ascii_letters))
#     list_of_letters.append(letter)
# print(list_of_letters)
# print(''.join(list_of_letters))

# podaj długość napisu
length = 10

# wygeneruj losowy ciąg alfabetyczny znaków o podanej długości
random_string = ''.join(random.choice(string.ascii_letters) for i in range(length))

# wyświetl wynik
print("Wygenerowany losowy ciąg alfabetyczny znaków:", random_string)

print("liczba z przedziału")

lower = 10
upper = 100

if lower > upper:
    print(random.randint(upper, lower))
else:
    print(random.randint(lower, upper))

print("Wielokrotnosc 7")

num = random.randint(1, 10)

multiple_of_7 = num * 7

print("Losowa wielokrotność liczby 7: ", multiple_of_7)


def losowa():
    losowa_liczba = random.randint(0, 10)
    wielokrotnosc = losowa_liczba * 7
    print("Wielokrotnosc_liczby_7:  ", wielokrotnosc)


wielokrotnosc_7 = [i * 7 for i in range(1, 11)]
print(wielokrotnosc_7)
print(random.choice(wielokrotnosc_7))
