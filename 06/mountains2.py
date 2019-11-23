mountains = {
    'Mount Everest' : 
        {'elevation': 8848, 'range':'Himalayas'},
    'K2' : 
        {'elevation': 8611, 'range':'Karakoram'},
    'Kangchenjunga' : 
        {'elevation': 8586, 'range':'Himalayas'},
    'Lhotse' : 
        {'elevation': 8516, 'range':'Himalayas'},
    'Makalu' : 
        {'elevation': 8485, 'range':'Himalayas'},
    }


print('\nMountains:')
for mountain in mountains:
    print(mountain)

print('\nElevation')
for elevation in mountains.values():
    print(elevation['elevation'])

print('\nRange')
for range in mountains.values():
    print(range['range'])

print('\nStatements')
for mountain, description in mountains.items():
    print("{} is an {}-meter tall mountain in the {} range.".format(mountain, description['elevation'], description['range']))