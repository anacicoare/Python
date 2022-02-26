import random
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

choice = random.randint(0, len(names))
buys_dinner = names[choice]

print(f"{buys_dinner} is going to buy the meal today!")
