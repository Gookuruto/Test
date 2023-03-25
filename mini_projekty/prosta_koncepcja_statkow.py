"""
kONCEPJA:
Stworzyc gre w statki. dla uproszczenia bedziemy mieli tylko pojedyncze statki.
- stworz plansze
- niech kazdy gracz rozmiesci statki(moga do siebie przylegac)
- rozpocznik gre kazdy gracz wpisuje gzie strzela np. a10
    - sprawdzane jest trafienie
        -jezeli trafil rysowana jest plansza z trafieniem i gracz ma kolejna szanse
        -jezeli nie to rysowana jest plansza dla drugiega gracza i petla sie powtarza dopoki ktorys z graczy nie przegra

- Dodaj mozliwosc poddania sie gracza.
- Dodaj mozliwosc zapisania stanu gry do pliku.(pomysl nad formatem) aby latwo bylo go potem zaladowac.
"""

class Ship:
    def __init__(self):
        self._size = 1
        self.position_x = None
        self.position_y = None

    def trafiony(self):
        self._size -=1
        print("trafiony")
        if self._size <1:
            self.zatopiony()

    def zatopiony(self):
        print("zatopiony!")