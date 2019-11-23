cisla = [1, 1, 2, 3, 5, 8, 13]
print(cisla)
for cislo in cisla:
    print(cislo)

seznam = [1, 'abc', True, None, range(10), len]
print(seznam)

for seznamy in seznam:
    print(seznamy)
print(cisla[2])
print(cisla[2:-3])

prvocisla = [2, 3, 5, 7, 11, 13, 17]
print(prvocisla)
prvocisla.append(19)
print(prvocisla)

a = [1, 2, 3]   # vytvoření seznamu
b = a           # tady se nový seznam nevytváří

# seznam vytvořený v prvním řádku má teď dvě jména: "a" a "b",
# ale stále pracujeme jenom s jedním seznamem

print(b)
a.append(4)
print(b)

dalsi_prvocisla = [23, 29, 31]
prvocisla.extend(dalsi_prvocisla)
print(prvocisla)

seznam = []
seznam.extend('abcdef')
seznam.extend(range(10))
print(seznam)