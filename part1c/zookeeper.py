from part1c.subjectInterface import *

class SubjectConcrete(Subject):
    ### apply the Observer Pattern by inheriting the subject interface and making a concrete subject
    def __init__(self):
        self.observerlist = []
        self.msg = 'NONE'

    def registerObserver(self, observer):
        if observer not in set(self.observerlist):
            self.observerlist.append(observer)
            print('Observer ' + observer.getName() + " got registered.")
        else:
            print("Observer already registered!")

    def removeObserver(self, observer):
        if observer in set(self.observerlist):
            self.observerlist.remove(observer)
            print('Observer ' + observer.getName() + " got removed.")
        else:
            print("Observer not found!")

    def stateChange(self, msg):
        self.msg = msg
        return self.msg

    def notifyObservers(self):
        for observer in self.observerlist:
            observer.update(self.stateChange(self.msg))


class Zookeeper(SubjectConcrete):

    def listObservers(self):
        """To list all the Observers, i.e. Zoo Announcers."""
        observernames = [observer.getName() for observer in self.observerlist]

        print('-> INFO ABOUT OBSERVERS:')
        if len(observernames) > 0:
            print("\tHere are the Observers: " + ', '.join(observernames))
        else:
            print("\tThere is no registered Observer any more.")

    # owls is sleeping when the zookeep wakes up animals.
    def wakeAnimals(self, animal_list):
        print('===========================================')
        msg = "The ZooKeeper is about to wake the animals."
        self.stateChange(msg)
        self.notifyObservers()
        print('===========================================')

        print('**Zookeeper is waking the animals**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ','+ animal.wakeUp())

    # owls is sleeping when the zookeep roll-calls animals.
    def rollCallAnimals(self, animal_list):
        print('===========================================')
        msg = "The ZooKeeper is about to roll call the animals."
        self.stateChange(msg)
        self.notifyObservers()
        print('===========================================')

        print('**Zookeeper is roll-calling the animals**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.makeNoise())

    # owls is sleeping when the zookeep feed animals.
    def feedAnimals(self, animal_list):
        print('===========================================')
        msg = "The ZooKeeper is about to feed the animals."
        self.stateChange(msg)
        self.notifyObservers()
        print('===========================================')

        print('**Zookeeper is feeding the animals**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ','+ animal.eat())

    # owls is sleeping when the zookeep exercises animals.
    def exerciseAnimals(self, animal_list):
        print('===========================================')
        msg = "The ZooKeeper is about to exercise the animals."
        self.stateChange(msg)
        self.notifyObservers()
        print('===========================================')

        print('**Zookeeper is exercising the animals**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.roam())

    # owls wake up when the zookeeper shuts down the zoo.
    def shutDownZoo(self, animal_list):
        print('===========================================')
        msg = "The ZooKeeper is about to shut down the zoo."
        self.stateChange(msg)
        self.notifyObservers()
        print('===========================================')

        print('**Zookeeper is shutting down the zoo**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.wakeUp())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())

