import random
def dice_roll():
    maxnumber = int(input("What would you like to roll out of?\n"))
    number_of_dice = int(input("How many dice would you like to roll?\n"))
    i = 1
    while i <= number_of_dice:
        rolls = []
        rolls.append(random.randint(1, maxnumber))
        i += 1
dice_roll()

class Player:
    def __init__(self, name, level, attack, intelligence, battle_intelligence, max_health,
            defense, speed, accuracy, stealth,action_number, bonus_action_number, max_encumbrance,):
        self.name = name
        self.level = level
        self.attack = attack
        self.intelligence = intelligence
        self.battle_intelligence = battle_intelligence
        self.max_health = max_health
        self.health = max_health
        self.defense = defense
        self.speed = speed
        self.accuracy = accuracy
        self.stealth = stealth
        self.action_number = action_number
        self.bonus_action_number = bonus_action_number
        self.max_encumbrance = max_encumbrance
        self.max_encumbrance = 0
        self.inventory = []
        self.weapons = []
        self.attack_type = self.weapons[0].damage_type
        self.armor = []
        self.movelist = []
        self.skills = []
        self.relations = {}
        self.init_attacks()

    def new_item(self, item):
        self.inventory.append(item)

    def new_weapon(self, weapon):
        self.weapons.append(weapon)

    def new_armor(self, armor):
        self.armor.append(armor)

    def entity_name(self):
        return self.name

    def moves(self):
        return self.moves

    def damaged(self, damage):
        self.health = max(self.health - damage, 0)
        print(f"{damage} damage done to {self.entity_name()}")

    def __str__(self):
        return f"A {self.level} level player named {self.name}, with {self.health} health."

class TutorialPlayer(Player):
    def init_attacks(self):
        self.attacks = []

class Item:
    pass

class Weapon:
    pass

class Armor:
    pass

class Move:
    pass
