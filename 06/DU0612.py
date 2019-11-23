from random import randrange

prvni_kolo =  '-------x------------'
druhe_kolo =  '-------x--o---------'
treti_kolo =  '-------xx-o---------'
ctvrte_kolo = '-------xxoo---------'
pate_kolo =   '------xxxxxxxxxxxxx-'

#pocitac má hraje s o

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    while True:
        cislo_policka = randrange(20)

        if pole[cislo_policka] == 'o' or pole[cislo_policka] == 'x':
            continue
        else:
            break

    return pole[:cislo_policka] + 'o' + pole[(cislo_policka + 1):]

print(pate_kolo)      
for i in range(50):
    print(tah_pocitace(pate_kolo))
