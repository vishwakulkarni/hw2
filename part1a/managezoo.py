from part1a.zooanimals import *
from part1a.zookeeper import *

### Felines ###
charlie = Cat("Charlie")
chloe = Cat("Chloe")
chris = Cat("Chris")

tom = Tiger("Tom")
ted = Tiger("Ted")

lucas = Lion("Lucas")
lincoln = Lion("Lincoln")

animal_list = [charlie, chloe, chris, tom, ted, lucas, lincoln]

### Pachyderms ###
evan = Elephant("Evan")
erik = Elephant("Erik")

hiro = Hippo("Hiro")
hillary = Hippo("Hillary")
hibai = Hippo("Hibai")

riley = Rhino("Riley")
robert = Rhino("Robert")

animal_list.extend([evan, erik, hiro, hillary, hibai, riley, robert])

### Canines ###
william = Wolf("William")
wayne = Wolf("Wayne")

dave = Dog("Dave")
daniel = Dog("Daniel")
drew = Dog("Drew")
dot = Dog("Dot")

animal_list.extend([william, wayne, dave, daniel, drew, dot])

### zookeeper ###
zkp = Zookeeper()
zkp.wakeAnimals(animal_list)
zkp.rollCallAnimals(animal_list)
zkp.feedAnimals(animal_list)
zkp.exerciseAnimals(animal_list)
zkp.shutDownZoo(animal_list)