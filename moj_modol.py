from random import shuffle

COLOURS = ["pik", "kier", "karo", "trefl"]
VALUES = [None, None, "2", "3", "4", "5", "6", "7", "8", "9",
          "10", "J", "Q", "K", "A"]

class Card:

    def __init__(self, value, colour):
        self.value = VALUES[value]
        self.colour = COLOURS[colour]

    def __repr__(self):
        return self.value + " " + self.colour

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):    # to są wartości kart - oczywiście z ich indeksów
            for j in range(4):   # to są kolory kart - z ich indeksów
                self.cards.append(Card(i, j))  # tu tworzymy karty
        shuffle(self.cards)  # a tu je losujemy

    def rm_card(self):
        if len(self.cards) == 0:  # będzie None jeśli talia będzie pusta
            return
        return self.cards.pop()  # a tu usuwamy kartę

deck = Deck()
for card in deck.cards:
    print(card)