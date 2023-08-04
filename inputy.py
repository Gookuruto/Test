#Z50
name = input("Podaj swoje imie: ")
print(f"Hello! {name}")
#Z51
number = input("Podaj swój wiek: ")
print(type(number))

#Z52
year = int(input("Podaj obecny rok: "))
print(f"Za 50 lat bedzie rok {year+50}")

#Z53
days = input("Podaj ilośc dni którą chcesz przekonwertowac na lata: ")
years = float(days)/365
# years = round(years,2)


print(f"{years:.2f}")
#
# #Z54
miles = input("Podaj ile mil chcesz przeliczyć na kilometry: ")
km = float(miles)*1.6
print(km)