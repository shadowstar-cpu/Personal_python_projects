'''Dice rolling and player creator for DnD or similar RPGs'''
import random
def dice_roll():
    '''produces a random number to simulate a dice roll, lets the user define the maximum number
    on the die ad the number of dice to roll'''
    maxnumber = int(input("What would you like to roll out of?\n"))
    number_of_dice = int(input("How many dice would you like to roll?\n"))
    i = 1
    rolls = []
    while i <= number_of_dice:
        rolls.append(random.randint(1, maxnumber))
        i += 1
    i = 0
    while i < len(rolls):
        print(rolls[i])
        i += 1
#dice_roll()

class Player:
    '''the superclass for all player type entities'''
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
        self.armor = []
        self.movelist = []
        self.skills = []
        self.relations = {}
        self.init_attacks()

    def new_item(self, item):
        '''a method to add a new item to the players inventory'''
        self.inventory.append(item)

    def new_weapon(self, weapon):
        '''a method to add a new weapon to the players equipped weapons'''
        self.weapons.append(weapon)

    def new_armor(self, armor):
        '''a method to add armor to the players equipped armor'''
        self.armor.append(armor)

    def new_move(self, move):
        '''a method to add moves to the players movelist'''
        self.movelist.append(move)

    def entity_name(self):
        '''returns the name of the entity'''
        return self.name

    def moves(self):
        '''returns a list of moves of the player'''
        return self.movelist

    def damaged(self, damage):
        '''subtracts the damage from the players health or sets it to zero if the damage would
        put it below zero'''
        self.health = max(self.health - damage, 0)
        print(f"{damage} damage done to {self.entity_name()}")

    def __str__(self):
        return f"A {self.level} level player named {self.name}, with {self.health} health"

class TutorialPlayer(Player):
    '''a tutorial player'''

    def init_attacks(self):
        '''initilizes attacks'''
        self.movelist = [Move('Strike', 100, 50)]

class Item:
    '''class for items'''


class Weapon:
    '''class for weapons'''

class Armor:
    '''class for armor'''

class Move:
    '''class for moves'''
    def __init__(self, name, power, accuracy):
        self.name = name
        self.power_percent = power
        self.accuracy = accuracy

    def __str__(self):
        return(f'A move named {self.name} with {self.power_percent}% of attack power'
               f' and {self.accuracy}% chance to hit.')

    def calculate_damage(self, attack_power):
        '''calculates the damage done'''
        if random.randint(1, 100) <= self.accuracy:
            max_damage = round(attack_power * self.power_percent / 100)
            return random.randint(1, max_damage)
        return 0
shadow = TutorialPlayer('Shadow', 20, 50, 50, 50, 300, 50, 50, 50, 50, 5, 10, 10000)
print(shadow)
print(f"shadow's moves {shadow.moves}")
