import abc

class ICharacter(abc.ABC):
    @abc.abstractmethod
    def attack(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def die(self):
        pass

class IAggressive:
    def aggro_to_enemy(self):
        pass

class Player(ICharacter):
    def attack(self):
        print("Gracz atakuje")

    def run(self):
        print("Gracz biegnie")

    def die(self):
        print("Gracz umiera")

class Monster(ICharacter,IAggressive):

    def die(self):
        print("Monster dying")

    def attack(self):
        print("Potwor atakuje")

    def run(self):
        print("Potwor biegnie")


player: ICharacter = Monster()

while True:
    command = input("Podaj komenede[run,die,attack]: ")
    if command == "run":
        player.run()
    elif command == "die":
        player.die()
    elif command == "attack":
        player.attack()
    else:
        print("Niepoprawna komenda")