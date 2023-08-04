import copy
import random

COLORS = ("kier", "trefl", "pik", "karo")
CARD_VALUES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


class Card:
    def __init__(self, color: str, value: str):
        self.color = color
        self.value = value

    def __repr__(self):
        return f"card: {self.value}:{self.color}"


class Deck:
    def __init__(self):
        self.shuffle()

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        self.cards = []
        for color in COLORS:
            for value in CARD_VALUES:
                self.cards.append(Card(color, value))
        random.shuffle(self.cards)

deck = Deck()

for i in copy.copy(deck.cards):
    print(deck.deal())

print(deck.cards)
deck.shuffle()
print(deck.cards)