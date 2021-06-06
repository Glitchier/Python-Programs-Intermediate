from turtle import *
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle=Paddle((-360,0))
r_paddle=Paddle((350,0))

screen.listen()
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

ball=Ball()
score_board=Scoreboard()

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y()

    if(ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    if(ball.xcor() > 380):
        ball.reset_ball()
        score_board.increase_score_l()
    if(ball.xcor() < -380):
        ball.reset_ball()
        score_board.increase_score_r()

screen.exitonclick()