#strana = input("Zadej délku strany čtverce") pro načtení string
#int(input("Zadej délku strany čtverce")) pro načtení celého čísla
#float(input("Zadej délku strany čtverce")) pro zadání desetiného čísla
strana = int(input("Zadej délku strany čtverce: "))
cislo_je_spravne = strana > 0
  
if cislo_je_spravne:
     print("Obvod čtverce se stranou",strana, "cm je", strana * 4, "cm")
    print("Obsah čtverce se stranou",strana, "cm je", strana * strana, "cm2")
else:
    print("Strana musí být kladná, jinak z toho nebude čtverec!")

print("Děkujeme za použití kalkulačky")

#Tento program počítá obvod a obsah čtverce.