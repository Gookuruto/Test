import random


class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"color: {self.color} value: {self.value}"

    def __repr__(self):
        return f"color {self.color} value {self.value}"


class CardTwo:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"color: {self.color} value: {self.value}"


CARD_COLORS = ["pik", "kier", "karo", "trefl"]
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

card = Card("pik", "A")
print(card)
card2 = [CardTwo("pik", "A")]
print(card2)


class Deck:
    def __init__(self):
        self.cards = []
        for color in CARD_COLORS:
            for value in CARD_VALUES:
                card = Card(color, value)
                self.cards.append(card)

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        self.cards.clear()
        for color in CARD_COLORS:
            for value in CARD_VALUES:
                card = Card(color, value)
                self.cards.append(card)
        random.shuffle(self.cards)

deck = Deck()
print(deck.cards)
print("Wyciagamy")
print(deck.deal())
print("Wyciaganelismy")
print(deck.cards)

print("Tasujemy")
deck.shuffle()
print(deck.cards)


