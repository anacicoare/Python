from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def game_over():
    message = Turtle()
    message.color("white")
    message.write("Game over!", align="center", font=("Arial", 24, "normal"))


screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
screen.update()
screen.screensize(600, 600)

screen.listen()

screen.onkey(snake.move_up, "Up")
screen.update()
screen.onkey(snake.move_down, "Down")
screen.update()
screen.onkey(snake.move_left, "Left")
screen.update()
screen.onkey(snake.move_right, "Right")
screen.update()

food = Food()
game_on = True
scoreboard = Scoreboard()

while game_on:
    snake.move_forward()
    time.sleep(0.1)
    screen.update()
    
    if food.distance(snake.segments[0]) < 15:
        scoreboard.add_point()
        
        new_food = Food()
        food.convert_to_seg()
        snake.add_segment(food)
        food = new_food
        food.move()
    
    if snake.detect_self_colision():
        break

    if snake.detect_wall_colision():
        break


game_over()
screen.exitonclick()

print(f"Congrats! Your final score is : {scoreboard.score}")
