class Zookeeper:

    # owls is sleeping when the zookeep wakes up animals.
    def wakeAnimals(self, animal_list):
        print('===================================')
        print('**Zookeeper is waking the animals**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ','+ animal.wakeUp())

    # owls is sleeping when the zookeep roll-calls animals.
    def rollCallAnimals(self, animal_list):
        print('\n-----------------------------------')
        print('**Zookeeper is roll-calling the animals**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.makeNoise())

    # owls is sleeping when the zookeep feed animals.
    def feedAnimals(self, animal_list):
        print('\n-----------------------------------')
        print('**Zookeeper is feeding the animals**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ','+ animal.eat())

    # owls is sleeping when the zookeep exercises animals.
    def exerciseAnimals(self, animal_list):
        print('\n-----------------------------------')
        print('**Zookeeper is exercising the animals**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.roam())

    # owls wake up when the zookeeper shuts down the zoo.
    def shutDownZoo(self, animal_list):
        print('\n-----------------------------------')
        print('**Zookeeper is shutting down the zoo**\n')
        for animal in animal_list:
            if animal.getType == 'Owl':
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.wakeUp())
            else:
                print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
        print('===================================')
