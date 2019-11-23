seznam = ["had", "andulka", "pes", "kočka", "králík"]

seznam_hodnot = []
sorted_seznam = []
final_seznam = []

for animal in seznam:
    seznam_hodnot.append([animal[1:], animal])

sorted_seznam = list(sorted(seznam_hodnot))

for animal in sorted_seznam:
    final_seznam.append(animal[1])

print(final_seznam)