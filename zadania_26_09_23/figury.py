import math


class Circle:
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return 2 * math.pi * self.promien

    def pole(self):
        return math.pi * self.promien ** 2

class Triangle:
    def __init__(self):
        pass


class Rectangle:
    def __init__(self):
        pass


class Square:
    def __init__(self):
        pass


class Figurka:
    def __init__(self, name, wysokosc, color, dzwiek):
        self.name = name
        self.wysokosc = wysokosc
        self.color = color
        self.dzwiek = dzwiek

    def wydaj_dzwiek(self):
        print(self.dzwiek)


charizard = Figurka("Charizard", 10, "orange", "Char!!!!!")
squirtle = Figurka("Squirtle", 10, "blue", "Squitle squirtle!")

print(charizard.name, charizard.color)
print(squirtle.name, squirtle.wysokosc)
charizard.wydaj_dzwiek()
squirtle.wydaj_dzwiek()

kolko = Circle(10)

print("obwod: %s" % kolko.obwod())
print(f"Pole koła o promieniu {kolko.promien}: {kolko.pole()}")
print(kolko.pole())
