# P4LAB1_EppersonCody_PartA.py
# Author: Cody Epperson
# Course: CTI110
# Description:
# This program uses turtle graphics and a for loop
# to draw a square and a triangle. Both shapes remain visible.

import turtle

# create the turtle
t = turtle.Turtle()
t.pensize(3)
t.speed(5)

# draw a blue square
t.color("blue")
for side in range(4):
    t.forward(100)
    t.right(90)

# move to a new spot so shapes don't completely overlap
t.penup()
t.goto(150, 0)
t.pendown()

# draw a red triangle
t.color("red")
for side in range(3):
    t.forward(100)
    t.left(120)

# finish up
t.hideturtle()
turtle.done()
