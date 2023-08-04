def dodaj_element(slownik):
    print(f"Aktualna zawartość słownika: {slownik}")
    klucz = input("Podaj nazwę elementu: ")
    wartosc = float(input("Podaj wartość elementu: "))
    slownik[klucz] = wartosc
    print("Element dodany do słownika.")
def usun_element(slownik):
    print(f"Aktualna zawartość słownika: {slownik}")
    klucz = input("Podaj nazwę elementu do usunięcia: ")
    if klucz in slownik:
        del slownik[klucz]
        print("Element usunięty ze słownika.")
    else:
        print("Element o podanej nazwie nie istnieje w słowniku.")
def edytuj_element(slownik):
    print(f"Aktualna zawartość słownika: {slownik}")
    klucz = input("Podaj nazwę elementu do edycji: ")
    if klucz in slownik:
        print(f"Aktualna wartość elementu '{klucz}': {slownik[klucz]}")
        nowa_wartosc = float(input("Podaj nową wartość elementu: "))
        slownik[klucz] = nowa_wartosc
        print("Element zaktualizowany.")
    else:
        print("Element o podanej nazwie nie istnieje w słowniku.")
wydatki = {}
przychody = {}
inwestycje = {}
while True:
    akcja = input("1 - podgląd, 2 - dodanie elementu, 3 - edycja wpisu, 4 - usunięcie wpisu, Q - wyjście z aplikacji ")
    if akcja == "2":
        kategoria = input("Wybierz kategorię (wydatki, przychody, inwestycje): ")
        if kategoria.lower() == "wydatki":
            dodaj_element(wydatki)
        elif kategoria.lower() == "przychody":
            dodaj_element(przychody)
        elif kategoria.lower() == "inwestycje":
            dodaj_element(inwestycje)
        else:
            print("Nieznana kategoria. Spróbuj ponownie.")
    elif akcja.upper() == "Q":
        break
    if akcja == "1":
        kategoria = input("Wybierz kategorię (wydatki, przychody, inwestycje): ")
        if kategoria.lower() == "wydatki":
            print(wydatki)
        elif kategoria.lower() == "przychody":
            print(przychody)
        elif kategoria.lower() == "inwestycje":
            print(inwestycje)
        else:
            print("Nieznana kategoria. Spróbuj ponownie.")
    elif akcja.upper() == "Q":
        break
    if akcja == "4":
        kategoria = input("Wybierz kategorię (wydatki, przychody, inwestycje): ")
        if kategoria.lower() == "wydatki":
            usun_element(wydatki)
        elif kategoria.lower() == "przychody":
            usun_element(przychody)
        elif kategoria.lower() == "inwestycje":
            usun_element(inwestycje)
    elif akcja.upper() == "Q":
        break
    if akcja == "3":
        kategoria = input("Wybierz kategorię (wydatki, przychody, inwestycje): ")
        if kategoria.lower() == "wydatki":
            edytuj_element(wydatki)
        elif kategoria.lower() == "przychody":
            edytuj_element(przychody)
        elif kategoria.lower() == "inwestycje":
            edytuj_element(inwestycje)
    elif akcja.upper() == "Q":
        break
print("Koniec programu.")