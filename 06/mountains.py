mountains = {
    'Mount Everest' : 8848,
    'K2' : 8611,
    'Kangchenjunga' : 8586,
    'Lhotse' : 8516,
    'Makalu' : 8485,
    }
def print_dict (slovnik):
    print()

print('Keys:')
for mountain in mountains:
    print(mountain)

print('\nHeights:')

for mountain in mountains.values():
    print(mountain)

print('\nStatements:')
for mountain, height in mountains.items():
    print(mountain, 'is', height ,'meters tall.')

print('\nSorted statements:')
for mountain, height in sorted(mountains.items()):
    print(mountain, 'is', height ,'meters tall.')    


mountains2 = {}
print('\nCreate new dictionary:')
for mountain, height in mountains.items():
    mountains2[mountain] = [height, height * 3.28]

print('\nMountains')
for mountain in mountains2:
    print(mountain)

print('\nMountains - meters')
for meter in mountains2.values():
    print(meter[0])  

print('\nMountains - feet')
for feet in mountains2.values():
    print(feet[1]) 

print('\Mountain statements:')
for mountain, height in mountains2.items():
    print(mountain, 'is', height[0] ,'meters tall, or',height[1],'feet.')   