from turtle import forward, exitonclick, left, right
from math import sqrt

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

exitonclick()    