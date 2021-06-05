from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def move(self):
        y_cor=self.ycor() + self.y_move
        x_cor=self.xcor() + self.x_move
        self.goto(x_cor,y_cor)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed*=0.8

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()