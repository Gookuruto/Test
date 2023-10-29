# 55
name = input("Podaj imie: ")
x = name.lower()
x = x.strip()
if "bond" in name.lower().strip():
    print("Welcome aboard agent 007.")
else:
    print(f"Good morning {name}")
#56
number = int(input("Podaj liczbe: "))

if number % 2 == 0:
    print("Parzysta!")
else:
    print("Nieparzysta!")

#custom

number = int(input("Podaj liczbe: "))

if number%3 ==0:
    print("Liczba podzielna przez 3")
elif number%2 == 0:
    print("liczba jest podzielna przez 2")
else:
    print("Liczba nie jest podzielna ani przez 3 ani przez 2")

dzielnik = 50
dzielniki= []
while dzielnik >1:
    if number%dzielnik == 0:
        dzielniki.append(dzielnik)
    dzielnik -=1
if dzielniki:
    print(f"Liczba jest podzielna przez {dzielniki[0]}")
else:
    print(f"liczba nie ejst pdozielna przez liczbe mniejsza lub rowna 50")

