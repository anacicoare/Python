import random

logo = '''                        _   _                                      _               
                                 | | | |                                    | |              
   __ _ _   _  ___  ___ ___      | |_| |__   ___       _ __  _   _ _ __ ___ | |__   ___ _ __ 
  / _` | | | |/ _ \/ __/ __|     | __| '_ \ / _ \     | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | (_| | |_| |  __/\__ \__ \     | |_| | | |  __/     | | | | |_| | | | | | | |_) |  __/ |   
  \__, |\__,_|\___||___/___/      \__|_| |_|\___|     |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
   __/ |                                                                                     
  |___/                                                                                      '''

def check(answer):
    global number_to_guess
    global finished
    global tries_left
    if int(number_to_guess) == int(answer):
        finished = 1
        print(f"Congrats! You guessed the number, {answer}!")
    elif int(answer) > int(number_to_guess):
        tries_left -= 1
        print(f"Wrong guess.\nYou have {tries_left} tries left.\nTry lower.")
    else:
        tries_left -=1
        print(f"Wrong guess.\nYou have {tries_left} tries left.\nTry higher.")

print(logo)
print("Welcome to the number guessing game.You will have to guess a number between 1 and 100.")
number_to_guess = random.randint(1,100)
difficulty = input("Choose the difficulty: 'easy' or 'hard' ").lower()

if difficulty == "easy":
        tries_left = 10
elif difficulty == "hard":
    tries_left = 5
while difficulty != "easy" and difficulty != "hard":
    if difficulty != "easy" and difficulty != "hard":
        print("You typed an incorrect difficulty.")
        difficulty = input("Type 'hard' or 'easy.'")
    if difficulty == "easy":
        tries_left = 10
    elif difficulty == "hard":
        tries_left = 5

finished = 0
while tries_left != 0 and finished == 0:
    print("\n")
    answer = input("Guess a number between 1 and 100.  ")
    check(answer)
    print("\n")
