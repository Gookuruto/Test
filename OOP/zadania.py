"""
1. Stworz pusta klase Vehicle
2. Do klasy vehicle dodaj atrybuty max_speed oraz mileage(przebieg)
3. Stworz klase pochodna od Vehicle ktora bedzie nazywac sie Bus i bedzie posiadaćwszystkie pola z Vehicle.
4. Dodaj do klasy Vehicle metode seating_capacity a następnie w klasie Bus spraw aby metoda seating_capacity miala domyślna wartość 50
5. Zdefiniuj atrybut klasowy „color” z domyślną wartością White. Oznacza to, że każdy Vehicle powinien być biały.
6. Utworz Klase pochodna Bus dziedzicząca po klasie Vehicle. z metoda wyliczajacą opłate(fare) dla klasy Bus powinno to byc
    final amount = total fare + 10% of the total fare. uzyj ponizszej klasy Vehicle:
        class Vehicle:
            def __init__(self, name, mileage, capacity):
                self.name = name
                self.mileage = mileage
                self.capacity = capacity

            def fare(self):
                return self.capacity * 100

        class Bus(Vehicle):
            pass

        School_bus = Bus("School Volvo", 12, 50)
        print("Total Bus fare is:", School_bus.fare())

7.Sprawdz jakiego typu jest zmienna School_bus:
    class Vehicle:
        def __init__(self, name, mileage, capacity):
            self.name = name
            self.mileage = mileage
            self.capacity = capacity

    class Bus(Vehicle):
        pass

    School_bus = Bus("School Volvo", 12, 50)

8. Sprawdź czy School_bus jest także instancją klasy Vehicle.
9. Mini projekt:
    -Stwórz klase dla kart do gry.
        -Klasa karty powinna mieć kolor (kiery, karo, trefl, pik) i wartość (A,2,3,4,5,6,7,8,9,10,J,Q,K)
    -Stwórz klase Talii ktora zawiera 52 karty
        -posiada metode deal ktora wyciaga karte z talii
        -po wyjeciu karty z talii karta powinna zostac z niej usunięta
        -posiada metode shuffle która upewnia się, że talia kart zawiera wszystkie 52 karty, a następnie losowo je przestawia.
        -
"""
import random


class Card:

    def __init__(self, color, value):
        self.value = value
        self.color = color

    def __repr__(self):
        return f"{self.value} of {self.color}"


class Deck:
    def __init__(self):
        colors = ["hearts", "diamonds", "clubs", "spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(color, value) for color in colors for value in values]

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("There is no cards.")

    def shuffle(self):
        random.shuffle(self.cards)

    def restart_deck(self):
        self.__init__()
        self.shuffle()

    def __repr__(self):
        return "Cards remaining in deck: {}".format(len(self.cards))


talia = Deck()
talie_2 = Deck()
print(talia is talie_2)
while True:
    talia.shuffle()
    if not talia.cards:
        kontynuawac = input("Czy kontynuowac(y/n): ")
        if kontynuawac == "y":
            talia.restart_deck()
            continue
        else:
            break
