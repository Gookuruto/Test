"""
Koncepcja:
1. Mamy 12 miesiecy wybieramy miesiac
2. w danym miesiacu mozemy dodac wydatek i wystwitlic wydatki (pomysl o dodatkowych funkcjach)
3. ... statystyki
"""

students = {
    "22117":{"name": "Jan", "surname": "Kowalski", "grades":{"Math": 4,"Geography":2}},
    "22116":{"name": "Maciej", "surname": "Kowalski", "grades":{"Math": 4,"Geography":2}},
    "22119":{"name": "Alicja", "surname": "Kowalska", "grades":{"Math": 4,"Geography":2}}
}

while True:
    print("[0] Dodaj studenta")
    print("[1] Usun studenta")
    print("[2] Edytuj studenta")
    print("[3] Wyswietl dane")
    print("[4] Exit")
    choice = input("Co chcesz zrobic[0-4]: ")
    if choice == "0":
        new_student = input("Podaj nowy indeks studenta: ")
        students[new_student] = {}
    elif choice == "1":
        student_to_remove = input("podej indeks studenta do usuniecia: ")
        del students[student_to_remove]
    elif choice == "2":
        index = input("podaj indeks studenta: ")
        change_value = input("co chcesz zminic?")
        new_calue = input("podaj nowe wartości: ")

        students[index][change_value] = new_calue
    elif choice == "3":
        for item in students.values():
            print(item)

    else:
        break