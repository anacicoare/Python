import turtle
from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(2.5, 1)
        self.speed(0)

    # initial position of the right paddle
    def move_right(self):
        coords = turtle.screensize()
        self.goto(coords[0], 0)
        self.speed(6)

    # initial position of the left paddle
    def move_left(self):
        coords = turtle.screensize()
        self.goto(-coords[0], 0)
        self.speed(6)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 10)
