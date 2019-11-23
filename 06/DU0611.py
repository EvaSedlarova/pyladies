prvni_kolo =  '-------x------------'
druhe_kolo =  '-------x--o---------'
treti_kolo =  '-------xx-o---------'
ctvrte_kolo = '-------xxoo---------'
pate_kolo =   '------xxxoo---------'

#Zadávat bude v rozmezí 1 - 20

def tah_hrace(pole, cislo_policka):
    "Vrátí herní pole se symbolem x umístěným na danou pozici"
    return pole[:(cislo_policka - 1)] + 'x' + pole[(cislo_policka):]

def zadej_pole(pole):
    while True:
        vstup_uzivatele = input("Zadej číslo pole v rozmezí od 1 do 20: ")
        try:
            cislo_policka = int(vstup_uzivatele)
        except ValueError:
            print("Nejedná se o číslo ve správném formátu")
            continue
        
        if cislo_policka not in range(1, 21, 1):
            print('Nejedná se o číslo v rozmezí 1 - 20')
            continue
        elif pole[cislo_policka - 1] == 'o' or pole[cislo_policka - 1] == 'x':
            print('Na tomto políčku se nemůže hrát.')
            continue
        else:
            break
          
    return cislo_policka
      
print(tah_hrace(prvni_kolo, zadej_pole(prvni_kolo)))

