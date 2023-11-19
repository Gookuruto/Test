from typing import List


class Animal:
    def __init__(self):
        self.name = "Zwirz"

    def sound(self):
        print("Animu Animu")


class Cat(Animal):
    def sound(self):
        print("mew mew")


class Dog(Animal):
    def sound(self):
        print("纬纬")

    def bite(self):
        pass


class Duck(Animal):
    def sound(self):
        print("Quack Quack")

    def eat(self):
        pass


lista_zwirzow: List[Animal] = [Duck(), Cat(), Animal(), Dog(), Duck(), Duck()]

for animal in lista_zwirzow:
    animal.sound()
    print(isinstance(animal, Cat))


autobus = Bus()
class Vehicle:
    def seating_capacity(self,capacity):
        return capacity
class Bus(Vehicle):
    def seating_capacity(self,magia(...)):
        return super().(...)

print(autobus.seating_capacity())