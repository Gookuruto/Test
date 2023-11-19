from typing import Literal, List


class Spider:
    def __init__(self):
        self.web = "Organic"

    def shoot_web(self):
        print(f"strzelam siecią")


class Man:
    def __init__(self):
        self.name = "Peter"
        self.height = 180
        self.weight = 80

    def introduce(self):
        print(f"Hello my name is {self.name}")


class SpiderMan(Spider, Man):
    def __init__(self):
        # super().__init__()
        super(SpiderMan, self).__init__()
        Man.__init__(self)
        self.costume = "Classic"

    def change_costume(self, new_costume: Literal["Classic", "Venom", "Noir", "Miles Morales"]):
        self.costume = new_costume

    def spider_sense(self):
        print("Sensing danger around.")

    def shoot_web(self):
        print("Shooting web from hands")


#Polimorfizm

humans: List[Man] = []
for i in range(20):
    if i % 3 == 0:
        humans.append(SpiderMan())
    else:
        humans.append(Man())

for human in humans:
    human.introduce()
