import random

class Character:
    def __init__(self, name, spec):
        self.name = name
        self.spec = spec

    inventory = []

    def combat(self):
        monsters = {1: "Dragon", 2: "Tainted Elf", 3: "Cursed Warlock"}
        loot = {1: "knife", 2: "sword", 3: "shield"}
        loot_roll = random.randint(1, 3)
        monster_roll = random.randint(1, 3)
        return print("{} engages in combat with {}! You receive {}".format(self.name, monsters[monster_roll], loot[loot_roll]))


character1 = Character("Nick", "Warrior")

print(character1.combat())







