from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name


    def setName(self, name):
        self.name = name


    def wakeUp(self):
        return " is waking up."


    @abstractmethod
    def makeNoise(self):
        pass


    def eat(self):
        return " is eating."


    @abstractmethod
    def roam(self):
        pass


    def sleep(self):
        return " is sleeping."


    def getName(self):
        return self.name


    @abstractmethod
    def getFamily(self):
        pass


    @abstractmethod
    def getType(self):
        pass
