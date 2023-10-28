"""
1.Napisz program który przeczyta cały plik teksowy.
2. Napisz program który przeczyta n pierwszych linii pliku teksowego.
3. Napisz program który wygeneruje losowo 100 liczb i zapisz do pliku w kazdej linii jedna liczbe i jej kwadrat
    liczba liczba**2
4. Napisz program w Pythonie, który doda tekst do pliku i wyświetli tekst pliku po dodaniu
5.Napisz program który znajdzie najdłuzsze słowo w pliku
6.Mając dwa pliki .txt zawierające listy liczb, znajdź liczby, które się nakładają.
"""

with open("abc.txt", "a+") as f:
    f.write("wpisany nowy text\n")
    print(f.read())

print("")
print("")

with open("abc.txt", "r") as f:
    print(f.read())

f = open("abc.txt", "a+")
f.write("Nowy super tekst\n")
f.close()