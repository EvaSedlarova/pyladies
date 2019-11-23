from turtle import forward, clear, exitonclick, left, right
from math import sqrt

user_input = input("Zadej n u n-úhelníku: ")

try:
    user_input = int(user_input)
except:
    print("Zadej celé číslo.")

for i in range(user_input):
    forward(200/user_input)
    left(360/user_input)

exitonclick()    