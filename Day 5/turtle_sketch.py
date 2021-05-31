from turtle import *

t=Turtle()
screen=Screen()

def move_forward():
    t.forward(10)
def move_backward():
    t.forward(-10)
def turn_left():
    new_heading=t.heading()+10
    t.setheading(new_heading)
def turn_right():
    new_heading=t.heading()-10
    t.setheading(new_heading)
def clr_scr():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clr_scr,"c")
screen.exitonclick()
