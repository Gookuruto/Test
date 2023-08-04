import copy
#
#
# class Car:
#     COLOR = "White"
#
#     def __init__(self, max_speed: int = 100):
#         self.__max_speed = max_speed
#
#     def accelerate(self):
#         print(f"Car is accelerating up to {self.__max_speed}")
#
#     @property
#     def max_speed(self):
#         return self.__max_speed
#
#     @max_speed.setter
#     def max_speed(self, max_speed):
#         if max_speed >= 0:
#             self.__max_speed = max_speed
#         else:
#             print("Do not drive in reverse gear.")
#
#
# def change_speed_to_zero(car: Car):
#     temp_car = copy.copy(car)
#     temp_car.max_speed = 0
#     return temp_car.max_speed
#
#
# def add_one(x: int):
#     x += 1
#     print(x)
#
#
# liczba = 1
# print(liczba)
# add_one(liczba)
# print(liczba)
# car_obj = Car()
#
# car_obj2 = Car(120)
# print(car_obj.max_speed)
#
# change_speed_to_zero(car_obj)
# print(car_obj.max_speed)
#
# car_obj.max_speed = -100
#
#
# class SportCar(Car):
#     def __init__(self, max_speed=250):
#         super().__init__(250)
#         self.bearking_force = 20
#
#     def breaking(self):
#         print(f"Car is breaking with force {self.bearking_force}")
#
#     # def accelerate(self):
#     #     super().accelerate()
#     #     print("from Sport car")
#
# sportcar = SportCar()
# sportcar.accelerate()
# sportcar.breaking()
# print(sportcar.max_speed)
# from typing import List
#
#
# class Bat:
#     def __init__(self):
#         self.food = "blood"
#
#     def atatck_evil(self):
#         print("im hunting")
#
#
# class Man:
#     def __init__(self):
#         self.name = "Bruce"
#         self.surname = "Wayne"
#         self.height = 185
#
#     def atatck_evil(self):
#         print("Atatcking evil.")
#
#
# class BatMan(Man, Bat):
#     def __init__(self):
#         super().__init__()
#         Bat.__init__(self)
#
#
# lst: List[Bat] = []
#
# lst.append(Bat())
# lst.append(BatMan())
#
# print(isinstance(BatMan(), Bat))
# print(isinstance(BatMan(), Man))
# print(isinstance(BatMan(), BatMan))
# print(isinstance(Man(), Bat))
# print(isinstance(Man(), BatMan))
#
# batman = BatMan()
# batman.atatck_evil()

