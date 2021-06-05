import random
from turtle import *
from color import color

direction=[0,90,180,270]

t=Turtle()
t.pensize(15)
t.shape("turtle")
t.color("DarkOrchid")
t.speed("fastest")
screen=Screen()

for i in range(200):
    t.pencolor(random.choice(color))
    t.forward(30)
    t.setheading(random.choice(direction))

screen.exitonclick()