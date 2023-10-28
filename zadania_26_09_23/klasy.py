import copy


class Car:
    def __init__(self, brand, model="Escort", max_speed=180):
        self.brand = brand
        self.model = model
        self.__speed = 0
        self.max_speed = max_speed

    def accelerate(self):
        print("We are accelerating")
        if self.__speed < self.max_speed:
            self.__speed += 10

    def press_break(self):
        print("we are breaking")
        if self.__speed > 0:
            self.__speed -= 10

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if 0 <= speed <= self.max_speed:
            self.__speed = speed
        else:
            print(f"We cannot go faster than {self.max_speed} and slower than 0")

    def __repr__(self):
        return f"{self.brand} {self.model}: {self.max_speed}, {self.__speed}"


nissan = Car("Nissan")# tworzymy obiekt Car i pokazujemy na niego

drugi_nissan = nissan# pokazujemy w to samo miejsce co zmienna nissan

print(nissan is drugi_nissan)
print(nissan)
print(drugi_nissan)
drugi_nissan.max_speed = 1000
print(nissan)
print(drugi_nissan)
