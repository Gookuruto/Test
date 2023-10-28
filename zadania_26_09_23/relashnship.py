import random
from typing import List, Optional, Any


class Human:
    def __init__(self, name, height, weight, hair_color, eyes_color):
        self.name = name
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eyes_color = eyes_color

    def inspect_person_relations(self, person: Any):
        """person should be of a class Woman."""
        person.be_inspected(self)

class Woman(Human):
    def __init__(self, height, weight, hair_color, eyes_color, name):
        super().__init__(name, height, weight, hair_color, eyes_color)
        self._partner: Optional[Human] = None
        self._friends: List[Human] = []

    @property
    def partner(self):
        if self._partner is not None:
            return self._partner.name

    @partner.setter
    def partner(self, partner):
        if partner.hair_color != "blonde":
            self._partner = self._partner
        else:
            self._partner = partner

    @property
    def friends(self):
        return

    def be_inspected(self, inspecting_person):
        if inspecting_person in self._friends:
            print(self.partner)
        else:
            print("Get off me.")


class Man(Human):
    def __init__(self, height, weight, hair_color, eyes_color, name):
        super().__init__(name, height, weight, hair_color, eyes_color)
        self._partner: Optional[Human] = None
        self._friends: List[Human] = []
        self.bread = False

    def get_partner(self):
        if self._partner is not None:
            return self._partner.name

    def set_partner(self, partner):
        if partner.hair_color != "red":
            self._partner = self._partner
        else:
            self._partner = partner


womans = ["Angelika", "Kasia", "Asia", "Zosia"]
mens = ["Sławek", "Jan", "Karol", "Paweł"]

hair_colors = ["red", "brown", "blonde", "other"]
womans_list = []
mans_list = []
for woman in womans:
    womans_list.append(Woman(165, 45, hair_colors[random.randint(0, len(hair_colors) - 1)], "blue", woman))

for man in mens:
    mans_list.append(Man(165, 45, hair_colors[random.randint(0, len(hair_colors) - 1)], "blue", man))

womans_list[0].partner = mans_list[-1]

print(womans_list[0].partner)

womans_list[0]._friends = [mans_list[1]]

mans_list[1].inspect_person_relations(womans_list[0])
