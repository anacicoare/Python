from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))