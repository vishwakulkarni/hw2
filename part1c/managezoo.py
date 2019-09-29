from part1c.zooanimals import *
from part1c.zookeeper import *
from part1c.zooannouncer import *


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

### Fish ###
tracy = Trout("Tracy")
trump = Trout("Trump")

kelly = Koi("Kelly")
kate = Koi("Kate")
kevin = Koi("Kevin")

bob = Bass("Bob")
bailey = Bass("Bailey")

animal_list.extend([tracy, trump, kelly, kate, kevin, bob, bailey])

### Birds ###
olivia = Owl("Olivia")
oscar = Owl("Oscar")

steve = Sparrow("Steve")
sam = Sparrow("Sam")

paul = Penguin("Paul")
polly = Penguin("Polly")
peter = Penguin("Peter")
piers = Penguin("Piers")

animal_list.extend([olivia, oscar, steve, sam, paul, polly, peter, piers])

### zooannouncers ###
zanc1 = ZooAnnouncer("Number#1")
zanc2 = ZooAnnouncer("Number#2")

### zookeeper ###
zkp = Zookeeper()

zkp.listObservers()

zkp.registerObserver(zanc1)
zkp.registerObserver(zanc2)

zkp.listObservers()

zkp.wakeAnimals(animal_list)
zkp.rollCallAnimals(animal_list)
zkp.feedAnimals(animal_list)
zkp.exerciseAnimals(animal_list)
zkp.shutDownZoo(animal_list)

zkp.removeObserver(zanc1)
zkp.removeObserver(zanc2)

zkp.listObservers()

del zanc1
del zanc2
