from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.len = 3
        self.segments = []
        for i in range(0,3):
            new_block = Turtle()
            new_block.penup()
            new_block.speed(1)
            new_block.shape("square")
            new_block.color("white")
            self.segments.append(new_block)
        x = self.segments[0].xcor()
        y = self.segments[0].ycor()
        for i in range(0,3):
            self.segments[i].goto(x,y)
            x -=20

    def move_body(self):
        for i in range(self.len - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x,y)

    def move_forward(self):
        self.move_body()
        self.segments[0].forward(20)

    def move_up(self):
        if self.segments[0].heading() != DOWN and self.segments[0].heading() != UP:
            self.move_body()
            self.segments[0].setheading(90)

    def move_left(self):
        if self.segments[0].heading() != RIGHT and self.segments[0].heading() != LEFT:
            self.move_body()
            self.segments[0].setheading(180)

    def move_down(self):
        if self.segments[0].heading() != UP and self.segments[0].heading() != DOWN:
            self.move_body()
            self.segments[0].setheading(270)
    
    def move_right(self):
        if self.segments[0].heading() != LEFT and self.segments[0].heading() != RIGHT:
            self.move_body()
            self.segments[0].setheading(0)
    
    def detect_self_colision(self):
        for i in range(3, self.len):
            if self.segments[0].distance(self.segments[i]) == 0:
                return True
        return False
    
    def detect_wall_colision(self):
        if self.segments[0].xcor() == 300 or self.segments[0].ycor() == 300 or self.segments[0].xcor() == -300 or self.segments[0].ycor() == -300:
            return True
        return False

    def add_segment(self, food):
        self.len += 1
        self.segments.append(food)

