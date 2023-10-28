# class Bat:
#     def __init__(self):
#         self.wings = 2
#
#     def introduce(self):
#         print("skrzek")
#
#
# class Man:
#     def __init__(self):
#         self.name = "Bruce"
#
#     def speak(self):
#         print("człowiek mówi.")
#
#
# class BatMan(Bat, Man):
#     def __init__(self):
#         super().__init__()
#         Man.__init__(self)
#         self.introduction = "Im batman"
#
#
# batman = BatMan()
#
# print(batman.wings)
# print(batman.name)
# print(batman.introduction)


class Vehicle:
    color = "White"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return capacity

    def fare(self):
        return self.seating_capacity(20) * 100


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def fare(self):
        base_fare = super(Bus, self).fare()
        return base_fare + (base_fare * 0.1)


pojazd = Vehicle(100, 100000)
van = Bus(150, 200000)

School_bus = Bus(100, 200000)

print(isinstance(School_bus, Vehicle))
