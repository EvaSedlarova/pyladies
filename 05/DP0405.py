seznam = ["had", "andulka", "pes", "kočka", "králík"]
seznam2 = ["had", "morče", "pes", "kočka", "prase"]

sjednoceni =[]
prvni = []
druhy =[]

sjednoceni = seznam + seznam2
print(sjednoceni)

for animal in seznam:
    if animal not in seznam2:
        prvni.append(animal)

print(prvni)

for animal in seznam2:
    if animal not in seznam:
        druhy.append(animal)

print(druhy)

print(sorted(seznam))
print(seznam)