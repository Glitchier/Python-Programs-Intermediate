from turtle import *
from color import color
import random

t=Turtle()
t.shape("turtle")
screen=Screen()

def ran_color():
    t_color=random.choice(color)
    return t_color

def draw_shapes(num_sides):
    angle=360/num_sides
    t.color(ran_color())
    for i in range(num_sides):
        t.forward(100)
        t.right(angle)

for i in range(3,10):
    draw_shapes(i)

screen.exitonclick()