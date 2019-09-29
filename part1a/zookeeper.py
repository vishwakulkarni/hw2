class Zookeeper:

    def wakeAnimals(self, animal_list):
        print('===================================')
        print('**Zookeeper is waking the animals**\n')
        for animal in animal_list:
            print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ','+ animal.wakeUp())

    def rollCallAnimals(self, animal_list):
        print('\n-----------------------------------')
        print('**Zookeeper is roll-calling the animals**\n')
        for animal in animal_list:
            print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.makeNoise())


    def feedAnimals(self, animal_list):
        print('\n-----------------------------------')
        print('**Zookeeper is feeding the animals**\n')
        for animal in animal_list:
            print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ','+ animal.eat())

    def exerciseAnimals(self, animal_list):
        print('\n-----------------------------------')
        print('**Zookeeper is exercising the animals**\n')
        for animal in animal_list:
            print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.roam())

    def shutDownZoo(self, animal_list):
        print('\n-----------------------------------')
        print('**Zookeeper is shutting down the zoo**\n')
        for animal in animal_list:
            print(animal.getName() + ', ' + animal.getType() + ', in family ' + animal.getFamily() + ',' + animal.sleep())
        print('===================================')
