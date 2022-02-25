# Love calculator
# first digit represents how many times the letters t,r,u,e are in either of their names
# second digit represents how many times the letters l,o,v,e are in either of their names
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

first_digit = name1.count('t') + name1.count('r') + \
    name1.count('u') + name1.count('e')
first_digit = first_digit + \
    name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')

second_digit = name1.count('l') + name1.count('o') + \
    name1.count('v') + name1.count('e')
second_digit = second_digit + \
    name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

score = str(first_digit) + str(second_digit)
additional_message = 0

if int(score) < 10 and int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
    additional_message = 1

if int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}, you are alright together.")
    additional_message = 1

if additional_message == 0:
    print(f"Your score is {score}.")
