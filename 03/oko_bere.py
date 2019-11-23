# Začínáš s 0 body.
# Počítač v každém kole vypíše, kolik máš bodů, a zeptá se tě, jestli chceš pokračovat.
# Pokud odpovíš „ne“, hra končí.
# Pokud odpovíš „ano“, počítač „otočí kartu“ (náhodně vybere číslo od 2 do 10), vypíše její hodnotu a přičte ji k bodům.
# Pokud máš víc než 21 bodů, prohráváš.
# Cílem hry je získat co nejvíc bodů, ideálně 21.
from random import randrange
score = 0
answer = 'ano'

while answer == 'ano':
    card = randrange(2,11)    
    print('Hodnota karty je:', card)
    score = score + card
    print("Celkový počet bodů je", score,'\n')
    if score > 21:
        print('Game over')
        break
    elif score == 21:
        print("Vyhráváš!")
        break
    answer = input("Chceš pokračovat? ano / ne\n")

    if answer != 'ano' and answer != 'ne':
        print("Tvoje odpověď není jasná, radši toho necháme.")
