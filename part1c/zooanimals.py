from random import randint

from part1c.animalfamily import *
from part1c.roamstrategy import *

"""
More animials are inhabited at the zoo:
Trout, Bass and Koi from the Fish family;
Owl, Sparrow and Penguin from the Bird family.
"""

### Felines ###
class Cat(Feline):

    def getType(self):
        return 'Cat'

    def catReactions(self):
        reactions = [' is eating like a Cat.', ' is making noise like a Cat.', ' is roaming like a Cat', ' is waking up.', ' is sleeping.']
        return reactions[randint(0, 4)]

    def eat(self):
        return self.catReactions()

    def makeNoise(self):
        return self.catReactions()

    def wakeUp(self):
        return self.catReactions()

    def roam(self):
        return self.catReactions()

    def sleep(self):
        return self.catReactions()

class Tiger(Feline):

    def getType(self):
        return "Tiger"

    def makeNoise(self):
        return " is making noise like a Tiger."

class Lion(Feline):

    def getType(self):
        return "Lion"

    # def roam(self):
    #     return " is roaming like a Lion."

    def makeNoise(self):
        return " is making noise like a Lion."


### Pachyderms ###
class Elephant(Pachyderm):

    def getType(self):
        return "Elephant"

    def makeNoise(self):
        return " is making noise like an Elephant."


class Hippo(Pachyderm):

    def getType(self):
        return "Hippo"

    # def roam(self):
    #     return " is roaming like a Hippo."

    def eat(self):
        return " is eating like a Hippo."

    def makeNoise(self):
        return " is making noise like a Hippo."

class Rhino(Pachyderm):

    def getType(self):
        return "Rhino"

    def sleep(self):
        return " is sleeping like a Rhino."

    def makeNoise(self):
        return " is making noise like a Rhino."


### Canines ###
class Wolf(Canine):

    def getType(self):
        return "Wolf"


class Dog(Canine):

    def getType(self):
        return "Dog"

    def wakeUp(self):
        return " is waking up like a Dog."

    def makeNoise(self):
        return " is making noise like a Dog."

    def eat(self):
        return " is eating like a Dog."

    # def roam(self):
    #     return " is roaming like a Dog."

    def sleep(self):
        return " is sleeping like a Dog."


### Fish ###
class Trout(Fish):

    def getType(self):
        return "Trout"

    def makeNoise(self):
        return " is making noise by jumping like a Trout."

    def sleep(self):
        return " is sleeping like a Trout."

class Bass(Fish):

    def getType(self):
        return "Bass"

    def eat(self):
        return " is eating like a Bass."

class Koi(Fish):

    def getType(self):
        return "Koi"

    def wakeUp(self):
        return " is waking up like a Koi."

### Birds ###
class Owl(Bird):

    def getType(self):
        return "Bird"

    def sleep(self):
        return " is sleeping like an Owl."

    def wakeUp(self):
        return " is waking up like an Owl."

    def makeNoise(self):
        return " is making noise like an Owl."

class Sparrow(Bird):

    def getType(self):
        return "Sparrow"

    def makeNoise(self):
        return " is making noise like a Sparrow."

class Penguin(Bird):

    def getType(self):
        return "Penguin"

    ### apply strategy
    # Penguins are different from other birds.
    # They roam in a normal way.
    # Penguins roam by referencing strategy RoamNormalStrategy()
    def roam(self):
        return RoamNormalStrategy().roam()

    def makeNoise(self):
        return " is making noise like a Penguin."