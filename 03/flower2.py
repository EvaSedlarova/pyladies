from turtle import left, right, shape, forward, exitonclick, penup, pendown

penup()
left(90)
forward(200)
right(90)
pendown()

right(90)

forward(40)
right(90)

for n in range(3):
    for r in range(2):
        for i in range(96//6):
            forward(2+n)
            right(360/96)            
        right(180-60)
    left(90)
    forward(30 + n)
    right(90)
     

#for number in range(18):

#    for cislo in range(4):
 #       forward(40)
  #      right(90)

   # right(20)



exitonclick()