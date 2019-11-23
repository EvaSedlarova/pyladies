from turtle import left, right, shape, forward, exitonclick, penup, pendown

penup()
left(90)
forward(150)
right(90)
pendown()

for number in range(18): #mandala

    for cislo in range(4):
         forward(40)
         right(90)

    right(20)

right(90) #přesouvám se na listy

forward(70)
left(90)

for n in range(6): #sety listů
    for r in range(2): #list vpravo
        for i in range(96//6): #list nahoru a dolů
            forward(2+n)
            left(360/96)            
        left(180-60)
    right(90)
    forward(15 + n)
    right(90)

    for r in range(2): #list vlevo
        for i in range(96//6): #list nahoru a dolů
            forward(2+n)
            right(360/96)            
        right(180-60)
    left(90)
    forward(15 + n)
    left(90) 

exitonclick()