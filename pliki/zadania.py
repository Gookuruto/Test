"""
1.Napisz program który przeczyta cały plik teksowy.
2. Napisz program który przeczyta n pierwszych linii pliku teksowego.
3. Napisz program który wygeneruje losowo 100 liczb i zapisz do pliku w kazdej linii jedna liczbe i jej kwadrat
    liczba liczba**2
4. Napisz program w Pythonie, który doda tekst do pliku i wyświetli tekst pliku po dodaniu
5.Napisz program który znajdzie najdłuzsze słowo w pliku
6.Napisz program w Pythonie, który generuje 26 plików tekstowych o nazwach A.txt, B.txt i tak dalej, aż do Z.txt.
7.Mając dwa pliki .txt zawierające listy liczb, znajdź liczby, które się nakładają.
 Jeden plik .txt zawiera listę wszystkich liczb pierwszych poniżej 1000, a drugi plik .txt zawiera listę szczęśliwych liczb do 1000.
"""
import time

# another_file = "abc.txt"
#
# with open(another_file, 'a+') as the_file:
#     for i in range(0, 15):
#         the_file.write("test 1\n")
#
# with open(another_file, 'r+') as the_file:
#     lines = the_file.readlines()
#     for line in lines:
#         print(line.strip())

with open("abc.txt", "a+", encoding="utf-8") as f:
    f.write("wpisany nowy text\n")
    print(f.read())

with open("abc.txt", "r", encoding="utf-8") as f:
    print(f.read())