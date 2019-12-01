class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{}: I like {}!".format(self.name, food))

class Kitten(Animal):
    def make_sound(self):
        print("{}: Meow!".format(self.name))
    
    def eat(self, food):
        print("{} looks at {}".format(self.name, food))
        super().eat(food)
 
class Puppy(Animal):
    def make_sound(self):
        print("{}: Woof!".format(self.name))

animals = [Kitten('Micka'), Puppy('Spot')]

for animal in animals:
    print(animal.name)
    animal.eat('meat')
    animal.make_sound()
    