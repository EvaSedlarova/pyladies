while True:
    rodne_cislo = input("Zadej rodné číslo ve formátu ******/****: ")   
    if rodne_cislo[:6].isdigit() and rodne_cislo[6] == "/" and rodne_cislo[7:].isdigit() and (int(rodne_cislo[:6] + rodne_cislo[7:]) % 11 ) == 0:
        break
    else:
        print("Špatný formát rodného čísla")
        
print("Rodné číslo je správné")

