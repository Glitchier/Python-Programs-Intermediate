from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score_board=Scoreboard()
snake=Snake()
food=Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 12 :
        food.refresh()
        snake.extend()
        score_board.if_coll()
    if (snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295) :
        score_board.reset()
        snake.reset()
    
    for seg in snake.segment[1:] :
        if snake.head.distance(seg) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()