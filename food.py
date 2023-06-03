from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid= 0.5)
        self.color("red")
        self.refresh()
    def refresh(self):
        x=random.randint(-280,280)
        y=random.randint(-280, 280)
        self.goto(x,y)

