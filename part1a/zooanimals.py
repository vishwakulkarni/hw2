from part1a.animalfamily import *
from random import randint

### Felines ###
class Cat(Feline):

    def getType(self):
        return 'Cat'

    def catReactions(self):
        reactions = [' is eating like a Cat.', ' is making noise like a Cat.', ' is roaming like a Feline.', ' is waking up.', ' is sleeping.']
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

    def roam(self):
        return " is roaming like a Lion."

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

    def roam(self):
        return " is roaming like a Hippo."

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

    def roam(self):
        return " is roaming like a Dog."

    def sleep(self):
        return " is sleeping like a Dog."