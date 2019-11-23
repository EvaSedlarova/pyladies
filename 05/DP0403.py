seznam = ["had", "andulka", "pes", "kočka", "králík"]
animals = []
animals2 = []
animals3= []
for animal in seznam:
    if len(animal) < 5:
        animals.append(animal)
        
print(animals)        

for animal in seznam:
    if animal[0] == "k":
        animals2.append(animal)
        
print(animals2)  

je_tam = input("vlož: ")
if je_tam in animals:
    print("True")
else:
    print("False")
        

for animal in seznam:
    if animal in animals:
        animals.append(animal)
