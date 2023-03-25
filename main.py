class Animal:

    def __init__(self, name: str = "", age: int = 10):
        self.__name = name  # ustawienie domyslnej wartosci pola name obiektu klasy Animal
        self.__age = age

    def print_details(self):  # metoda wypisujaca stan obiektu
        print(f"Imie: {self.__name}, wiek: {self.__age}.")

    def set_age(self, age: int):
        if age > 0:
            self.__age = age
        else:
            print("age must be greater than 0")

    def get_age(self):
        return self.__age


kot = Animal("Czarek", 4)
czarek = kot

print(kot is czarek)
czarek.print_details()
czarek.set_age(100)
czarek.print_details()
kot.print_details()
