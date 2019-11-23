small = int(input("Zadej číslo: "))
for i in range(4):
    number = int(input("Zadej další číslo: "))
    if number < small:
        small = number

print("Nejmenší číslo je",small)