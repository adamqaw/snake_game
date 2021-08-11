from turtle import Turtle
import random

cor_list = []
for cor in range(-280, 280):
    if cor % 20 == 0:
        cor_list.append(cor)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = (random.choice(cor_list))
        random_y = (random.choice(cor_list))
        self.goto(random_x, random_y)
