from math import pi

a = 5
b = 10
vyska = 10

def obsah_elipsy(a, b):
    return pi*a*b

def objem_eliptickeho_valce(vyska):
    return vyska * obsah_elipsy(a,b)

print("Objem eliptického válce je", objem_eliptickeho_valce(vyska), "cm3")