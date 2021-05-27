import random
from turtle import *

#return RGB tuple
def ran_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_tuple=(r,g,b)
    return color_tuple

def draw_spiro(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t.pencolor(ran_color())
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)

t=Turtle()
t.shape("turtle")
t.color("DarkOrchid")
t.speed("fastest")

#screen mode should be 255 to implement RGB color mode
screen=Screen()
screen.colormode(255)

draw_spiro(5)

screen.exitonclick()