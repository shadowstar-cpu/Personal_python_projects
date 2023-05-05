import random
def Dice_roll():
    Max = int(input("What would you like to roll out of?\n"))
    Number_of_dice = int(input("How many dice would you like to roll?\n"))
    i = 1
    while i <= Number_of_dice:
        Roll = random.randint(1, Max)
        print(Roll)
        i += 1
Dice_roll()

class Player:
    def __init__(self, name, level, attack, intelligence, battle_intelligence, max_health, defense, speed, accuracy, stealth, action_number, bonus_action_number, max_encumbrance,):
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
        self.armor = []
        self.moves = []
        self.skills = []
        self.relations = {}
    
    def new_item(item):
        self.inventory.append(item)
    
    def new_weapon(weapon):
        self.inventory.append(weapon)

    def new_armor(armor):
        self.inventory.append(armor)
    
    def __str__(self):
        return f""        

class Ranger(Player):
    pass
class Warrior(Player):
    pass

class item:
    pass
    
class weapon:
    pass

class armor:
    pass