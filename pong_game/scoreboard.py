from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-200, 300)
        self.write("0   0", True, align="center", font=('Calibri', 80, 'bold'))

    def write_score(self, score1, score2):
        self.clear()
        self.goto(-200, 300)
        self.write(f"{score1}   {score2}", True, align="center", font=('Calibri', 80, 'bold'))

    def write_message(self, message):
        self.clear()
        self.goto(0, 0)
        self.write(message, True, align="center", font=('Calibri', 80, 'bold'))