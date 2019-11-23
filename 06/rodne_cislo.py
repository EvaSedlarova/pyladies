# Domácí úkol
# Přepiš program na kontrolu rodného čísla tak, aby odpovídal následujícímu zadání. Chování programu z pohledu uživatele by mělo zůstat stejné, změní se jenom zápis kódu uvnitř.

# Napiš tyto funkce. Každá z nich dostane jako argument řetězec s rodným číslem a nějak ho zanalyzuje:

# (a) Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vrací True nebo False)
# (b) Je dělitelné jedenácti? (vrací True nebo False)
# (c) Jaké datum narození je v čísle zakódováno? (vrací trojici čísel – den, měsíc, rok)
# (d) Jaké pohlaví je v čísle zakódováno? (vrací 'muž' nebo 'žena')
# Pro účely úkolu stačí, když bude program umět zpracovat čísla vydávaná od roku 1985. Reálná rodná čísla můžou být složitější :)

# Napiš program který se uživatele zeptá na rodné číslo a vypíše výsledky.

# (a) správný formát - číslice + lomítko + číslice
def format(rodne_cislo):
    """ Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vrací True nebo False) """
    return len(rodne_cislo) == 11 and rodne_cislo[:6].isdigit() and rodne_cislo[6] == "/" and rodne_cislo[7:].isdigit()


def delitelne_jedenacti(rodne_cislo):
    """ Je dělitelné jedenácti? (vrací True nebo False) """
    return (int(rodne_cislo[:6] + rodne_cislo[7:]) % 11 ) == 0


def datum_narozeni(rodne_cislo):
    """ Jaké datum narození je v čísle zakódováno? (vrací datum narození – den, měsíc, rok) """
    if int(rodne_cislo[:2]) >=85: # ročníky nad 1985
        if int(rodne_cislo[2]) in [5, 6]: #žena
            print(rodne_cislo[4:6] + '.' + str(int(rodne_cislo[2]) - 5 ) + rodne_cislo[3] + '.' + '19' + rodne_cislo[:2])
        
        elif int(rodne_cislo[2]) in [0, 1]: #muž
            print(rodne_cislo[4:6] + '.' + rodne_cislo[2:4] + '.' + '19' + rodne_cislo[:2])
           
        else:
            print("Zkontroluj si číslice x a 4.")
     

    elif int(rodne_cislo[:2]) < 54: #ročníky pod 2054
        if int(rodne_cislo[2]) in [5, 6]: #žena
            print(rodne_cislo[4:6] + '.' + str(int(rodne_cislo[2]) - 5 ) + rodne_cislo[3] + '.' + '20' + rodne_cislo[:2])
          
        elif int(rodne_cislo[2]) in [0, 1]: #muž
            print(rodne_cislo[4:6] + '.' + rodne_cislo[2:4] + '.' + '20' + rodne_cislo[:2])
            
        else:
            print("Zkontroluj si číslice 3 a 4.")
           
    else:
        print("Z tohoto rodného číslo bohužel datum narození neurčím")
       


def pohlavi(rodne_cislo):
    """ Jaké pohlaví je v čísle zakódováno? (vrací 'muž' nebo 'žena') """
    if int(rodne_cislo[2]) in {5, 6}:
        print("Žena")
        
    elif int(rodne_cislo[2]) in {0, 1}:
        print("Muž")
        
    else:
        print("Toto pohlaví neexistuje")   
        

def analyza_rodneho_cisla():
    while True:
        rodne_cislo = input("Zadej rodné číslo ve formátu ******/****: ") 

        if format(rodne_cislo) and delitelne_jedenacti(rodne_cislo):
            print("Rodné číslo je ve správném formátu")
            break
        print("Rodné číslo je ve špatném formátu.")
            

    datum_narozeni(rodne_cislo)
    pohlavi(rodne_cislo)
           
analyza_rodneho_cisla()