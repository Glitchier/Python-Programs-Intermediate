from turtle import Turtle


from turtle import *

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("Seagreen")
        self.shape("turtle")
        self.reset_position()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
    
    def finish_line(self):
        if(self.ycor() > FINISH_LINE_Y):
            return True
        else:
            return False