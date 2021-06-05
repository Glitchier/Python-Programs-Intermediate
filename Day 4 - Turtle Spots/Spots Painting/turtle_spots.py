import random
from turtle import *
import colorgram

colors=colorgram.extract('palette.jpg',30)
t=Turtle()

#screen mode should be 255 to implement RGB color mode
screen=Screen()
screen.colormode(255)

#extracting colors from image using colorgram
def RGB_Color():
    rgb_colors=[]
    for i in colors:
        r=i.rgb.r
        g=i.rgb.g
        b=i.rgb.b
        new_color=(r,g,b)
        rgb_colors.append(new_color)
    return rgb_colors

t.penup()
t.shape("turtle")
t.color("seagreen")
t.speed("fastest")
t.setheading(225)
t.forward(300)
t.setheading(0)
num_of_dots=101

for i in range(1,num_of_dots):
    t.dot(20,random.choice(RGB_Color()))
    t.forward(50)

    if(i%10==0):
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen.exitonclick()