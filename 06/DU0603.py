from turtle import forward, exitonclick, left, right
from math import sqrt, atan, degrees

def uhlopricka(lenght, height):
    return sqrt(lenght**2 + height**2)


def house(lenght, height):
    
    forward(lenght)
    left(90)
    forward(height)
    left(90)
    forward(lenght)
    left(90)
    forward(height)

    left(180 - degrees(atan(lenght/height)))
    forward(uhlopricka(lenght, height))

    left(2 * degrees(atan(lenght/height)))
    
    forward(uhlopricka(lenght, height) / 2)
    
    left((90 - degrees(atan(lenght/height))) * 2)
    forward(uhlopricka(lenght, height) / 2)

    left(2 * degrees(atan(lenght/height)))
    
    forward(uhlopricka(lenght, height))

    left(90 - degrees(atan(lenght/height)))
    forward(lenght)

house(120, 50)
exitonclick()    