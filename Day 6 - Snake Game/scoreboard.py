from turtle import *

ALIGN="center"
FONT=("Arial",18,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}",align=ALIGN,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGN,font=FONT)

    def if_coll(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Arial",18,"normal"))