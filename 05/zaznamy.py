zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

""" Snadný způsob jak zjistit, zda je řetězec složen jen z malých písmen,
je metoda islower(), která vrací True, pokud řetězec obsahuje jen malá písmena,
jinak vrací False. Například 'abc'.islower() == True ale 'aBc'.islower() == False.

Snadný způsob, jak převést první písmenko na velké
je metoda capitalize(): např. 'abc'.capitalize() == 'Abc' """
jmena = []
chybne_zaznamy = []
spravne_zaznamy = []
opravene_zaznamy = []


#for i in zaznamy:
for i in range(len(zaznamy)):
        jmena.append(zaznamy[i].split())
       
        if  jmena[i][0][0].islower() or jmena[i][1][0].islower():
            chybne_zaznamy.append(jmena[i][0] + " "  + jmena[i][1])
            opravene_zaznamy.append(jmena[i][0].capitalize() + " "  + jmena[i][1].capitalize())
        else:
            spravne_zaznamy.append(jmena[i][0] + " "  + jmena[i][1])
            opravene_zaznamy.append(jmena[i][0] + " "  + jmena[i][1])

print(chybne_zaznamy)
print(spravne_zaznamy)
print(opravene_zaznamy)