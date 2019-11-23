prvni_kolo =  '-------x------------'
druhe_kolo =  '-------x--o---------'
treti_kolo =  '-------xx-o---------'
ctvrte_kolo = '-------xxoo---------'
pate_kolo =   '------xxxoo---------'

#Bude nutné ohlídat, aby cislo_policka nepřepsalo minulý symbol a nebylo mimo hrací pole
#Otázka je, bude uživatel zadávat v rozmezí 0 - 19 nebo 1 a 20 - v druhém případě musím upravit kód

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    return pole[:cislo_policka] + symbol + pole[(cislo_policka + 1):]

print(tah(prvni_kolo, 19, 'x'))

