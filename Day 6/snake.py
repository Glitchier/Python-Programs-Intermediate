from turtle import *

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=15
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segments(pos)    

    def add_segments(self,pos):
        new_turtle=Turtle("square")
        new_turtle.shapesize(stretch_wid=0.8,stretch_len=0.8)
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(pos)
        self.segment.append(new_turtle)

    def extend(self):
        self.add_segments(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            x_cor=self.segment[seg_num-1].xcor()
            y_cor=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(x_cor,y_cor)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)
    
    def down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(DOWN)
    
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)
    
    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(RIGHT)