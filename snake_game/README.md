SNAKE GAME

I have recreated the snake game. The player is represented as a snake and by
"eating" points in grows in length. When the snake's head touches its body the game ends.
The game also ends when the snake's head crashes into the walls.

I have created this app using OOP concepts such as inheritance and abstraction. This app 
is based on the turtle module. All the snake's segments are turtles, and I have defined basic
movement methods. The key of the movements is that the snake's segments begin moving from the 
back (from n-1 to 0) so that the direction of the head dictates the whole body's direction.

The food is a Turtle class inherited object. When the snake's head comes very close to the
food, it converts in a snake segment that is added to the back of the player.

I also created a Scoreboard that inherits the Turtle class. It writes the score on the screen
and updates it every time the length of the snake increases. At the end of the game it also
writes "Game over!".