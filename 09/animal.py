class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{}: I like {}!".format(self.name, food))

class Kitten(Animal):
    def meow(self):
        print("{}: Meow!".format(self.name))
   
 
class Puppy(Animal):
    def woof(self):
        print("{}: Woof!".format(self.name))

micka = Kitten('Micka')
spot = Puppy('Spot')

micka.meow()
spot.woof()

micka.eat('rat')
spot.eat('cat')