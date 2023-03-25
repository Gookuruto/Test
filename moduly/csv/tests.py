import  csv

pola = []
wiersze = []
with open('employees.csv') as plikCSV:
    czytnikCSV = csv.reader(plikCSV,delimiter=',')


    #wczytujemy nagłówki
    pola = next(czytnikCSV)

    #wczytujemy dane
    wiersze = [wiersz for wiersz in czytnikCSV]

    print(pola)
    # print(wiersze[0])
    print(type(pola))
    print(type(wiersze))
    for i in range (1,50):
        print(wiersze[i])



    #liczymy srednia
    suma = 0
    for wiersz in wiersze:
        suma += int(wiersz[7])
    srednia = suma/len(wiersze)
    print(f'Srednia płaca to: {srednia}$')
    print(f'Ilość wierszy w bazie to: {len(wiersze)}')

def wiersze_w_liniach():
    for i in range (1,50):
        print(wiersze[i])

plik_TXT = open("kopia_płac.txt", "w")
if plik_TXT.writable():
    plik_TXT.write(f'{pola}\n')
    for i in range(1,50):
        plik_TXT.write(f'{wiersze[i]}\n')
plik_TXT.close()