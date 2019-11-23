prvni_kolo =  '-------x------------'
druhe_kolo =  '-------x--o---------'
treti_kolo =  '-------xx-o---------'
ctvrte_kolo = '-------xxoo---------'
pate_kolo =   '------xxxoo---------'

# Nepotřebuji jít až na konec pole stačí mi, když skončím u třetího od konce

def stav_hry(pole, hrac):
    "Vrátí True, pokud jsou tři stejné znaky za sebou a False, pokud ne"
    for i in range(len(pole) - 2):
        if pole[i] == hrac and pole[i + 1] == hrac and pole[i + 2] == hrac:
            return True
    return False

def vyhodnot(pole):
    "Vrátí, v jakém stavu je pole, jestli někdo vyhrál, zda hra skončila nebo stále pokračuje"
    if stav_hry(pole, 'x'):
        return 'x'
    elif stav_hry(pole, 'o'):
        return 'o'
    elif '-' in pole:
        return '-'
    else:
        return '!'

print(vyhodnot(prvni_kolo))
print(vyhodnot(druhe_kolo)) 
print(vyhodnot(treti_kolo)) 
print(vyhodnot(ctvrte_kolo)) 
print(vyhodnot(pate_kolo))      