from part1b.animal import Animal
from part1b.roamstrategy import *

"""
In addition to Feline, Pachyderm and Canine,
this module has two more family animals: Fish and Bird.

Fish roam by swimming;
Birds roam by flying;
Feline, Pachyderm and Canine roam in a normal way.
"""



class Feline(Animal):

    def getFamily(self):
        return 'Feline'

    ### apply strategy
    # Felines roam by referencing strategy RoamNormalStrategy()
    def roam(self):
        return RoamNormalStrategy().roam()


    def eat(self):
        return " is eating like a Feline."

class Pachyderm(Animal):

    def getFamily(self):
        return "Pachderm"

    ### apply strategy
    # Pachyderms roam by referencing strategy RoamNormalStrategy()
    def roam(self):
        return RoamNormalStrategy().roam()

    def eat(self):
        return " is eating like a Pachyderm."

class Canine(Animal):

    def getFamily(self):
        return "Canine"

    ### apply strategy
    # Canines roam by referencing strategy RoamNormalStrategy()
    def roam(self):
        return RoamNormalStrategy().roam()

    def wakeUp(self):
        return " is waking up like a Canine."

    def makeNoise(self):
        return " is making noise like a Canine."

class Fish(Animal):

    def getFamily(self):
        return "Fish"

    def makeNoise(self):
        return " is making noise by jumpling like a Fish."

    ### apply strategy
    # Fish roam by referencing strategy RoamBySwimStrategy()
    def roam(self):
        return RoamBySwimStrategy().roam()

class Bird(Animal):

    def getFamily(self):
        return "Bird"

    ### apply strategy
    # Birds roam by referencing strategy RoamByFlyStrategy()
    def roam(self):
        return RoamByFlyStrategy().roam()

    def sleep(self):
        return " is sleeping like a Bird."
