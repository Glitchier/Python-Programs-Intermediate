from turtle import *
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x_cor=random.randint(-290,290)
        y_cor=random.randint(-290,290)
        self.goto(x_cor,y_cor)
        self.refresh()
    
    def refresh(self):
        x_cor=random.randint(-290,290)
        y_cor=random.randint(-290,290)
        self.goto(x_cor,y_cor)