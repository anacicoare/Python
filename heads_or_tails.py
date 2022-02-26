import random

guess = input("Heads or tails?").lower()

if guess == "heads":
    guess = 0
elif guess == "tails":
    guess = 1

random_integer = random.randint(0,1)
if guess == random_integer:
    print("You won!")
else:
    print("You lost!")