# 90
print("Zadanie 90")


class Vehicle:
    pass


veh = Vehicle()
print(veh)
# 91
print("Zadanie 91")


class Vehicle:
    def __init__(self):
        self.max_speed = 100
        self.mileage = 100000


veh = Vehicle()
print(f"{veh.max_speed} {veh.mileage}")
# 92
print("Zadanie 92")


class Bus(Vehicle):
    def __init__(self):
        super().__init__()


bus = Bus()

print(f"{bus.max_speed} {bus.mileage}")
# 93
print("Zadanie 93")


class Vehicle:
    def __init__(self):
        self.max_speed = 100
        self.mileage = 100000

    def seating_capacity(self, cap):
        return cap


class Bus(Vehicle):
    def __init__(self):
        super().__init__()

    def seating_capacity(self, cap=50):
        return super().seating_capacity(cap)


bus = Bus()
veh = Vehicle()

print(bus.seating_capacity())
print(bus.seating_capacity(100))

# 94
print("Zadanie 94")


class Vehicle:
    color = "White"

    def __init__(self):
        self.max_speed = 100
        self.mileage = 100000

    def seating_capacity(self, cap):
        return cap


class Bus(Vehicle):
    def __init__(self):
        super().__init__()

    def seating_capacity(self, cap=50):
        return super().seating_capacity(cap)


bus = Bus()
veh = Vehicle()
veh2 = Vehicle()

Vehicle.color = "Blue"  # zmienamy klase (atrybut klasowy)
veh.color = "Black"  # przesłaniamy atrybut klasowy atrybutem obiektu
print(f"Bus {bus.color}")
print(f"veh {veh.color}")
print(f"veh2 {veh2.color}")
# 95
print("Zadanie 95")


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() * 1.1


School_bus = Bus(" School Volvo ", 12, 50)
print(" Total Bus fare is :", School_bus.fare())
# 96
print("Zadanie 96")
print(type(School_bus))
# 97
print("Zadanie 97")
print(isinstance(School_bus, Vehicle))


class Notes:
    def __init__(self, id, text, completed=False):
        self.id = id
        self.text = text
        self.completed = completed
