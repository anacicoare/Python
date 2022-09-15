import turtle
from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def detect_collision(self, paddle):
        coords = turtle.screensize()
        return self.distance(paddle) < 50 and abs(self.xcor()) > 390

    def start_ball(self):
        angle = randint(-45, 45)
        self.setheading(angle)

    def change_direction(self):
        current_angle = self.heading()

        new_angle = 180 - current_angle

        self.setheading(new_angle)

    def h_change_direction(self):
        current_angle = self.heading()
        new_angle = - current_angle
        self.setheading(new_angle)





