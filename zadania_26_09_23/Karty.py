import random


class Karta:

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"Color: {self.color}, Value: {self.value}"


class Deck:
    def __init__(self):
        self.karty = []
        self.shuffle()

    def shuffle(self):
        kolory = ["kier", "karo", "trefl", "pik"]
        wartosci = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for kolor in kolory:
            for wartosc in wartosci:
                karta = Karta(kolor, wartosc)
                self.karty.append(karta)
        random.shuffle(self.karty)

    def deal(self):
        if self.karty:
            return self.karty.pop()
        else:
            return "no more cards"


talia = Deck()

talia_2 = Deck()
print(talia is talia_2)

talia.shuffle()

while True:
    print(talia.deal())
    if not talia.karty:
        kontynuowac = input("Czy kontynuowac?(y/n): ")
        if kontynuowac == "y":
            talia.shuffle()
            continue
        else:
            break
