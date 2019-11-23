class Kitten:
    def meow(self):
        print("Meow!")
    def eat(self, food):
        print("{}: Meow meow! I like {}!".format(self.name, food))
 
# Vytvořené konkrétního objektu
kitten = Kitten()

# Volání metody
kitten.meow()

mourek = Kitten()
mourek.name ='Mourek'

micka = Kitten()
micka.name ='Micka'


print(micka.name)
print(mourek.name)
micka.eat('rats )