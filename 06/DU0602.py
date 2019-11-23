from turtle import forward, exitonclick, left, right
from math import sqrt

def house(lenght):
    for i in range (3):
        forward(lenght)
        left(90)

    forward(lenght)

    left(135)
    forward(lenght*sqrt(2))

    for i in range(2):
        left(90)
        forward(lenght*sqrt(2)/2)

    left(90)
    forward(lenght*sqrt(2))

    left(45)
    forward(lenght)

house(10)
house(50)
house(80)

exitonclick()    