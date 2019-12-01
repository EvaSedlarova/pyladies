class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{}: I like {}!".format(self.name, food))

class Kitten(Animal):
    def meow(self):
        print("{}: Meow!".format(self.name))
    
    def eat(self, food):
        print("{} looks at {}".format(self.name, food))
        super().eat(food)
 
class Puppy(Animal):
    def woof(self):
        print("{}: Woof!".format(self.name))

class Snake(Animal):
    def __init__(self, name):
        name = name. replace('s', 'sss')
        name = name. replace('S', 'Sss')
        super().__init__(name)

micka = Kitten('Micka')
spot = Puppy('Spot')
standa = Snake('Stanislav')

micka.meow()
spot.woof()

micka.eat('milk')
spot.eat('bone')
standa.eat('mouse')