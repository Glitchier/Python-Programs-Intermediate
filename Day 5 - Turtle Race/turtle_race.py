from turtle import *
import random
import turtle

screen=Screen()
screen.setup(width=500,height=500)
user_bet=screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race?").lower()

colors=["red","orange","yellow","green","blue","purple"]
y_pos=[-80,-40,0,40,80,120]
no_of_turtles=[]

for i in range(len(colors)):
    t=Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230,y=y_pos[i])
    no_of_turtles.append(t)

if user_bet:
    race_on=True

while race_on:
    for i in no_of_turtles:
        if i.xcor() > 230:
            race_on=False
            winning_color=i.pencolor()
            if(winning_color==user_bet):
                print(f"You Win. The {winning_color} turtle is the winner.")
            else:
                print(f"You Lose. The {winning_color} turtle is the winner.")
        random_distance=random.randint(0,10)
        i.forward(random_distance)

screen.exitonclick()

