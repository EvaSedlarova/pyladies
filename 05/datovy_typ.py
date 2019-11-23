cisla = [1, 1, 2, 3, 5, 8, 13]

print(cisla[2:-3]) #konečný řetězec se nezapočítává
print(cisla[-3])

cisla = [1, 2, 3, 4, 5, 6]
del cisla[-1]
print(cisla)
del cisla[3:5]
print(cisla)
del cisla
print(cisla)