#Xochitl Martinez
#CS175L
#STOP

import math
import turtle

window_width = 400
window_height = 400
animation_speed = 0
num_sides = 8
length = 100
angle = 45
text_x = -5
text_y = -10

turtle.setup(window_width, window_height)

s = length
x = s / math.sqrt(2)
diameter = s + (2 * x)

sign = turtle.Turtle()
sign.speed(animation_speed)

sign.penup()
sign.goto(-55, 125)
sign.pendown()
sign.fillcolor("red")
sign.begin_fill()

for f in range(1,num_sides+1):
    sign.forward(length)
    sign.right(angle)
sign.end_fill()

sign.penup()
sign.goto(-51, -107)
sign.pendown()
sign.begin_fill()

for a in range(0, num_sides):
    sign.color("white")
    sign.fillcolor("white")
    sign.forward(93)
    sign.left(angle)
sign.end_fill()

sign.penup()
sign.goto(-46, -97)
sign.pendown()
sign.begin_fill()

for l in range(0, num_sides):
    sign.color("red")
    sign.fillcolor("red")
    sign.forward(85)
    sign.left(angle)
sign.end_fill()

sign.penup()
sign.penup()
sign.goto(3, -25)
sign.color("white")
sign.write("STOP", align = "center", font = ("Rimes New Roman", "56"))
#Rimes New Roman is a new font i accidentally discovered
sign.hideturtle()
