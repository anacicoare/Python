import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_input = input("What do you choose? Rock, paper or scissors?").lower()
choice_computer = random.randint(0,2)

if choice_input == "rock":
    choice_int = 0
elif choice_input == "paper":
    choice_int = 1
elif choice_input == "scissors":
    choice_int = 2

choice_list = [rock, paper, scissors]

print(f"\nYou chose\n{choice_list[choice_int]}\n")
print(f"\nComputer chose\n{choice_list[choice_computer]}\n")

ok=0
if choice_int == choice_computer:
    print("\nIt's a draw\n")
    ok=1
if choice_int > choice_computer or (choice_int == 0 and choice_computer == 2):
    print("\nYou win!\n")
    ok=1
if ok == 0:
    print("\nYou lose!\n")
