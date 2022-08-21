from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("triangle")
        self.shapesize(0.5, 0.5)
        self.color("red")
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)

    def move(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)

    def convert_to_seg(self):
        self.speed(1)
        self.shape("square")
        self.color("white")
        self.shapesize(1,1)