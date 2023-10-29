#50
print("Zadanie 50")

ans_1 = input("Podaj swoje imie: ")

print(" Hello !, " + ans_1)

#51
print("Zadanie 51")
ans_1 = int(input("Podaj swój wiek: "))

print(type(ans_1))
#52
print("Zadanie 52")
try:
    year = int(input("Podaj rok: "))
except ValueError:
    print("Bledna wartość")

print(year + 50)
#53
print("Zadanie 53")
days = int(input("Podaj ilość dni: "))

result = days/365

print(f"{days} dni to {result} lat")
#54
print("Zadanie 54")
exception = True
while exception:
    exception = False
    try:
        miles = float(input("Podaj ilość mil: "))
    except:
        exception = True
        print("Wpisz poprawna warotśc liczbowa")

result = miles*1.6

print(f"{miles} mil to {result} km")