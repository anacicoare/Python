import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from dashed_line import Line
from scoreboard import Scoreboard
from ball import Ball
import time


def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10


def init_screen(screen):
    screen.bgcolor("black")
    screen.tracer(0)
    screentk = screen.getcanvas().winfo_toplevel()
    screentk.attributes("-fullscreen", True)


def r_move_up():
    r_paddle.sety(r_paddle.ycor() + 40)
    screen.update()


def r_move_down():
    r_paddle.sety(r_paddle.ycor() - 40)
    screen.update()


def l_move_up():
    l_paddle.sety(l_paddle.ycor() + 40)
    screen.update()


def l_move_down():
    l_paddle.sety(l_paddle.ycor() - 40)
    screen.update()


# set screen
screen = Screen()
init_screen(screen)

# initialise paddles
l_paddle = Paddle()
r_paddle = Paddle()
l_paddle.move_left()
r_paddle.move_right()

# initialise middle separator line
line = Line()

# initialise score
score = Scoreboard()
p1 = 0    # left paddle's score
p2 = 0    # right paddle's score

# initialise ball
pong = Ball()

# initialise screen commands
screen.tracer(0)
screen.onkeypress(l_move_up, "w")
screen.update()
screen.onkeypress(l_move_down, "s")
screen.update()
screen.onkeypress(r_move_up, "Up")
screen.update()
screen.onkeypress(r_move_down, "Down")
screen.update()

# start game
game_on = True
pong.start_ball()
speed = 5
while game_on:
    screen.listen()
    time.sleep(0.01)
    pong.forward(speed)
    screen.update()

    # if it gets past a paddle
    if abs(pong.xcor()) > 500:
        break

    coords = turtle.screensize()

    # if it touches the right paddle
    if pong.detect_collision(r_paddle):
        pong.change_direction()
        speed += 0.5
        p2 += 1

    # if it touches the left paddle
    if pong.detect_collision(l_paddle):
        pong.change_direction()
        speed += 0.5
        p1 += 1

    # wall collision
    if abs(pong.ycor()) > 400:
        pong.h_change_direction()

    score.write_score(p1, p2)

# now the game has ended

# extract the winning player
if p1 > p2:
    p1 = -1
else:
    p2 = -1

# show game over message
if p1 == -1:
    score.write_message("Game over! Player 1 has won!")
else:
    score.write_message("Game over! Player 2 has won!")

# exit statement
screen.exitonclick()

