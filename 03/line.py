from turtle import left, right, shape, forward, exitonclick, penup, pendown

shape('turtle')

for cislo in range(30):
    forward(5+cislo)
    penup()
    forward(5)
    pendown()
    left(18)

exitonclick()