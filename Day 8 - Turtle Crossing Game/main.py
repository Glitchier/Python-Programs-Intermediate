from turtle import *
import time
from player import Player
from cars import CarManager
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player_turtle=Player()
screen.listen()
screen.onkeypress(player_turtle.move,"Up")

car_manager=CarManager()
score_board=Scoreboard()

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    for cars in car_manager.all_cars:
        if(cars.distance(player_turtle) < 20):
            game_on=False
            score_board.game_over()

    if player_turtle.finish_line():
        player_turtle.reset_position()
        car_manager.level_up()
        score_board.level_plus()

screen.exitonclick()
