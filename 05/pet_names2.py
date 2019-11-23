names_animals = {
    'kocour': 'Mates',
    'pes': 'Fík',
    'pták': 'Vrkal',
    'prase': 'Čvachta',
    }
names_animals['kocour'] = 'Tlapka'

for animal, name in names_animals.items():
    print("{} je {}".format(name, animal))


names_animals['ještěr'] = 'Godzilla'

for animal, name in names_animals.items():
    print("{} je {}".format(name, animal))

del names_animals['pes'] 

for animal, name in names_animals.items():
    print("{} je {}".format(name, animal))
