import random
from turtle import *

#return RGB tuple
def ran_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_tuple=(r,g,b)
    return color_tuple

direction=[0,90,180,270]

t=Turtle()
t.pensize(15)
t.shape("turtle")
t.color("DarkOrchid")
t.speed("fastest")

#screen mode should be 255 to implement RGB color mode
screen=Screen()
screen.colormode(255)

for i in range(200):
    t.pencolor(ran_color())
    t.forward(30)
    t.setheading(random.choice(direction))

screen.exitonclick()