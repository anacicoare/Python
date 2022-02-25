# Treasure Island game
# Game based on choices
print('''
*******************************************************************************
          | | | |
 _________ | ________________.=""_;=.______________ | _____________________ | _______
| |, -"_,=""     `"=. | |
| ___________________ | __"=._o`"-._        `"=.______________ | ___________________
          | `"=._o`"=._      _`"=._ |
 _________ | _____________________:=._o "=._."_. -= "'"=.__________________ | _______
| |    __.--" , ; `"=._o." ,-"""-._ ". |
|___________________ | _._"  ,. .` ` `` ,  `"-._"-._   ". '__ | ___________________
          |           |o`"=._` , "` `; .". ,  "-._"- ._;;              |
 _________|___________ |; `-.o`"=._; ." ` '`."\` . "-._ / _______________|_______
| | | o;    `"-.o`"=._``  '` ", __.--o; |
|___________________|_ | ;     (  # ) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___ | o; ._    "      `".o | o_.--"; o; ____/______/______/____
/ ______/______/______/_"=._o--._; | ;        ; ; / ______/______/______/_
____/______/______/______/__"=._o--._; o | o;     _._; o; ____/______/______/____
/ ______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/ ______/______/______/______/______/______/______/______/______/______/[TomekK]
** *****************************************************************************
''')
print("Welcome to the Treasure Island! Your mission is to find the treasure.")

direction = input(
    "You are at a crossroad. What direction do you want to go?\nType left or right.\n").lower()
if direction == "left":
    swim = input(
        "You have to get on the other side of the river. Do you swim there or wait for a boat?\nType swim or wait.\n").lower()
    if swim == "wait":
        door = input(
            "The magic boat teleported you inside a castle. You have to choose a door.\nType which one you choose: blue, red, yellow.").lower()
        valid_input = 0
        if door == "red" or door == "blue" or door == "yellow":
            valid_input=1
        if valid_input == 1:
            if door == "red":
                print("You have been burnt by fire.\nGame over.")
            elif door == "blue":
                print("You have been eaten by beasts.\nGame over.")
            elif door == "yellow":
                print("The treasure is all yours! Good job!")
        else:
            print("Game over.")
    else:
        print("You were attacked by a trout.\nGame over.")
else:
    print("You fell into a hole.\nGame over.")
