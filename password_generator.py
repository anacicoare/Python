#it has the order of characters randomised
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

characters= [letters, numbers, symbols]            #created list to randomly select what to put next in the password

letters.append(nr_letters)
numbers.append(nr_numbers)
symbols.append(nr_symbols)                         # added the number of elements to take at the end of the lists

chosen_set = random.choice(characters)
chosen_element = random.choice(chosen_set)
chosen_set[len(chosen_set) - 1] -= 1
password = str(chosen_element)                      #first character of password as a string

while (letters[len(letters) - 1] != 0) or (numbers[len(numbers) - 1] != 0) or (symbols[len(symbols) - 1] != 0):
    chosen_set = random.choice(characters)
    if chosen_set[len(chosen_set) - 1] != 0:        #if we didn't already use them up already
        chosen_element = random.choice(chosen_set)
        chosen_set[len(chosen_set)-1] -= 1          #we eliminate the one we have chosen
        password = password + str(chosen_element)   #add to the password

print(password)                                     #final password