class Kitten:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("Meow!")

    def eat(self, food):
        print("{}: Meow meow! I like {}!".format(self.name, food))
 


mourek = Kitten('Mourek')
mourek.meow()
mourek.eat('rats')

print(mourek)