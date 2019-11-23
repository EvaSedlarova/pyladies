from turtle import setposition, left, right, speed, hideturtle, forward, color, penup, pendown, bgcolor, begin_fill, end_fill
from random import randrange

speed(0)  # rychlost kreslení, rozmezí 0 - 10, 0 je téměř okamžitá, 10 nejrychlejší, 1 nejpomalejší
hideturtle()  # schová šipku
bgcolor('Midnight Blue')  # barva pozadí
colors = ['Dark Goldenrod', 'Goldenrod', 'Light Goldenrod', 'Gold', 'Light Yellow']  # možné barvy hvězdy


while True:  # nekonečně generuje nové hvězdy
    penup()
    setposition(randrange(-300,300),randrange(-300,300))  # náhodný výbět pozice budoucí hvězdy
    pendown()
    
    color('Midnight Blue', colors[randrange(len(colors))])  # náhodný výběr barvy hvězdy, počet barev pomocí len()
    n = randrange(5,8)  # kolik má hvězda cípů

    begin_fill()  # začíná vybarvovat    

    for i in range(n):  # tvorba hvězdy
        
        forward(300 / n**2)  # dělím mocninou aby při více cípech hvězdy byly násobně menší strany
        left(360 * 2/n)
        forward(300 / n**2)  
        right(360/n)  
    
    end_fill() # končí vybarvovat
 
 
