class Kitten:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("{}: Meow!".format(self.name))

    def eat(self, food):
        print("{}: Meow meow! I like {}!".format(self.name, food))
 
class Puppy:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("{}: Woof!".format(self.name))

    def eat(self, food):
        print("{}: Meow meow! I like {}!".format(self.name, food))
 
