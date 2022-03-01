import random
from hangman_art import hangman,word_list,hangman_logo

word = random.choice(word_list)
found_word = []

for i in range(len(word)):
    found_word.append("_ ")

string_word = ""
for character in found_word:
    string_word += character

print(hangman_logo)
print("Welcome to the hangman game!")
print(string_word)

not_completed = True
wrongs = 0
while not_completed:
 print(f"\nYou have {6-wrongs} guesses left.\n")
 print(hangman[wrongs])
 guessed_letter = input("Guess a letter: ")
 
 if len(guessed_letter) == 1:
     valid_input = True
 else:
     valid_input = False
 
 if valid_input:
        
        got_letter = False
        if word.find(guessed_letter) == -1:
            wrongs += 1
            print(f"\n\n\n\nYou guessed {guessed_letter}, sorry that's not in the word.")
        else:
            for pos,letter in enumerate(word):
                if letter == guessed_letter:
                    found_word[pos] = guessed_letter
                    got_letter = True
        
        if got_letter:
            print("\n\n\n\nNice guess!")

        if not("_ " in found_word):
            not_completed = False
        
        string_word = ""
        
        for character in found_word:
            string_word += character 
        
        print(string_word )
 else:
     input("You typed wrong, type anything to continue guessing ")
 
 if wrongs == len(hangman) - 1:
     print(hangman[wrongs])
     print("Game over! You lost!")
     not_completed = False 
 
if wrongs < len(hangman) - 1:
    print("Congrats! You won!")
