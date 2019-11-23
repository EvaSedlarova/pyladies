import turtle
import random
from turtle import penup, pendown , circle, setpos, begin_fill, end_fill, color

colors = ["red", "blue","green", "purple", "yellow", "orange", "black"]



for x in range(5):
    randColor = random.randrange(0, 7)
    rand1 = random.randrange(-300,300)
    rand2 = random.randrange(-300,300)
       
    color(colors[randColor])

    penup()
    setpos((rand1, rand2))
    pendown()
       
    begin_fill()
    circle(random.randrange(0,80))
    end_fill()