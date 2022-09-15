from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super(Line, self).__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color("white")
        init_y = 450
        up = True

        while init_y > -450:
            self.goto(0, init_y)
            init_y -= 10
            if up:
                self.pendown()
            else:
                self.penup()
            up = not up
