from part1a.animal import Animal

class Feline(Animal):

    def getFamily(self):
        return 'Feline'

    def roam(self):
        return " is roaming like a Feline."

    def eat(self):
        return " is eating like a Feline."

class Pachyderm(Animal):

    def getFamily(self):
        return "Pachderm"

    def eat(self):
        return " is eating like a Pachyderm."

class Canine(Animal):

    def getFamily(self):
        return "Canine"

    def wakeUp(self):
        return " is waking up like a Canine."

    def makeNoise(self):
        return " is making noise like a Canine."
