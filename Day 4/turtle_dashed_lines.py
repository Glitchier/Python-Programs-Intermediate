from turtle import *

turtle_ob=Turtle()
turtle_ob.shape("turtle")
turtle_ob.color("#FF666E")

screen=Screen()

for i in range(15):
    turtle_ob.forward(10)
    turtle_ob.penup()
    turtle_ob.forward(10)
    turtle_ob.pendown()


screen.exitonclick()