"""Napiš si třídy pro cokoliv chceš tak, aby splňovaly zadání:

* Jedna rodičovská třída, kde bude alespoň jeden atribut a jedna metoda
* Dvě (nebo více) odvozených tříd
* Jedna odvozená třída bude kompletně přepisovat metodu nadřazené třídy
* Druhá odvozená třída bude rozšiřovat metodu nadřazené třídy pomocí super()
* Obě odvozené třídy budou mít stejnou metodu, která bude dělat stejnou věc jiným způsobem
(koťátko mňouká, štěňátko štěká)"""


class Starship:
    def __init__(self, name, shields = 100):
        self.assignation = name
        self._shields = shields
    
    @property
    def shields(self):
        return self._shields

    @shields.setter
    def shields(self, value):
        if not 0 <= value <= 100 :
            raise ValueError("Shields can have value of 0 to 100 only.")
        self._shields = value

    def attack(self):
        print("{} is attacking.".format(self.assignation))

    def damage_to_shields(self, attack):
        if self.shields > attack:
            self.shields -= attack
        else:
            self.shields = 0
           
    def victory(self):
        print("All of {}'screens are showing fireworks" .format(self.assignation))   
 
class Fighter(Starship):

    def attack(self, arsenal):
        super().attack()
        print("{}s were fired!".format(arsenal))

    def victory(self):
        print("{} did a barrel roll" .format(self.assignation))   

class Transport(Starship):

    def attack(self):
        print("{} - all defensive capabilities are employed and defensive manouvers are underway".format(self.assignation))   


    def victory(self):
        print("All occupants of {} are relieved" .format(self.assignation))   
    
        
starships = [Transport("Falcon", 90), Fighter("TIE Advanced x1", 100)]

starships[0].attack()
starships[1].attack("High calibre round")

starships[0].damage_to_shields(20)
starships[1].damage_to_shields(90)

for starship in starships:
    print("Status: {} has shields at {} % ". format(starship.assignation, starship.shields))

print("{} retreated!".format(starships[1].assignation))

starships[0].victory()

