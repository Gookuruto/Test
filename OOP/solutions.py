class Vehicle:

    def __init__(self, max_speed: float, mileage: float, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"seating capacity is {capacity}"

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self, max_speed, mileage,capacity):
        super().__init__(max_speed, mileage,capacity)

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def fare(self):
        return super().fare()*1.1


class Car(Vehicle):
    pass

bus = Bus(100, 90,10)
pojazd = Vehicle(1, 1,10)

print(pojazd.fare())
print(bus.fare())
