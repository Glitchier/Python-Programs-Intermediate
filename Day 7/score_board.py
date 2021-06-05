from turtle import *

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l=0
        self.score_r=0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100,210)
        self.write(self.score_l,align="center",font=("Arial",60,"normal"))
        self.goto(100,210)
        self.write(self.score_r,align="center",font=("Arial",60,"normal"))
    
    def increase_score_l(self):
        self.score_l+=1
        self.update_score()
    
    def increase_score_r(self):
        self.score_r+=1
        self.update_score()