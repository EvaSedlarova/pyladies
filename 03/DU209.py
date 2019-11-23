from random import randrange

cislo_tahu = randrange(3)

if cislo_tahu == 0:
    tah_pocitace = 'kámen'
elif cislo_tahu == 1:
    tah_pocitace = 'nůžky'
else:
    tah_pocitace = 'papír'

tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_pocitace == tah_cloveka:
     print('Plichta.')
elif (tah_cloveka == 'kámen' and tah_pocitace == 'nůžky') or (tah_cloveka == 'nůžky' and tah_pocitace == 'papír') or (tah_cloveka == 'papír' and tah_pocitace == 'kámen'):
    print('Vyhrála jsi')  
elif tah_cloveka == 'kámen' or tah_cloveka == 'nůžky' or tah_cloveka == 'papír':
    print('Počítač vyhrál')  
else:
    print('Nerozumín')