# 90
class Vehicle:
    pass


# 91
class Vehicle:
    #94
    color = "White"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    # 93
    def seating_capacity(self, capacity: int):
        return f"seating capacity is {capacity}"

    def fare(self):


# 92
class Bus(Vehicle):
    def __init__(self, mileage):
        super().__init__(90, mileage)

    # 93
    def seating_capacity(self, capacity: int = 50):
        return super().seating_capacity(capacity)


#
bus = Bus(100000)
print(bus.seating_capacity())
# print(bus.max_speed, bus.mileage)
