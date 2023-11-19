# class Car:
#     def __init__(self, model: str, engine: str = "V8", color: str = "White"):
#         self.model = model
#         self.engine = engine
#         self.color = color
#         self.speed = None
#
#     def jedz(self):
#         self.speed = 100
#         print(self.speed)
#
#
# audi = Car("Audi A8")
#
# print(audi.speed)
# print(f"{audi.model} {audi.engine} {audi.color}")
#
# nissan = Car("nissan GTR", "3.0 twin turbo", "Black")
#
# print(f"{nissan.model} {nissan.engine} {nissan.color}")
#
# print(audi is nissan)


class Animal:
    def __init__(self, name="Rex", age=2):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Wstawiasz głupoty!")

    def print_details(self):
        print(f"Name: {self.name} Age: {self._age}")


class Cats(Animal):
    def __init__(self):
        super().__init__()
        self.lifes = 9

    def print_details(self):
        print(f"Cats with lifes: {self.lifes}")
        super().print_details()


pudelko = Animal()
pudelko_2 = pudelko
pudelko_2.age = 10
print(pudelko.age)
pudelko_2.age = -20

kotek = Cats()
kotek.print_details()


pudelko.print_details()
