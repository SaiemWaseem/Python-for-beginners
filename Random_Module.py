# Random Module

import random
members = ["Sam","Sami","Sammy"]
leader = random.choice(members)
print(leader)
import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
dice.roll()
print(dice.roll())



