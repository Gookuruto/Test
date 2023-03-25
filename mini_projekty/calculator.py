class Calculator:
    def __init__(self, constant):
        self.constant_factor = constant

    def add(self, a, b):
        return (a + b)*self.constant_factor

    def sub(self, a, b):
        return a - b

print(cal.add(1,2))