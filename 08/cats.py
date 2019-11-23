# Teď, když už umíš dělat koťátka, zkus vytvořit třídu pro kočku.

# Kočka umí mňoukat metodou meow.
# Kočka má na začátku (při vytvoření) 9 životů (nemůže mít nikdy víc než 9 nebo míň než 0!).
# Kočka umí říct, jestli je živá (nemá 0 životů), metodou is_alive.
# Kočka může ztratit život metodou lose_life.
# Kočku můžeš nakrmit metodou eat, která bere 1 argument - nějaké konkrétní jídlo (řetězec). Pokud je toto jídlo "fish", kočce se obnoví jeden život (pokud teda už není mrtvá, nebo nemá maximální počet životů).

class Kitten:
    def __init__(self, name):
        self.name = name
        self.lives = 9

    def meow(self):
        print("Meow!")

    def is_alive(self):
        return self.lives > 0                

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
        if not self.is_alive():        
            print("{} is dead.".format(self.name))

    def eat(self, food):
        if 0 < self.lives < 9 and food == 'fish':
            self.lives += 1
            

mourek = Kitten('Mourek')

for i in range(8):
    mourek.lose_life()

print(mourek.lives)
for i in range(15):
    mourek.eat('fish')
print(mourek.lives)
print(mourek.is_alive())