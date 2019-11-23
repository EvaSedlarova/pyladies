from turtle import forward, exitonclick, left, right
from math import sqrt

for h in range(10):
    for i in range (3):
        forward(50)
        left(90)

    forward(50)

    left(135)
    forward(50*sqrt(2))

    for i in range(2):
        left(90)
        forward(50*sqrt(2)/2)

    left(90)
    forward(50*sqrt(2))
    left(45)
    forward(10)

exitonclick()    