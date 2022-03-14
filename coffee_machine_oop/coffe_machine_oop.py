from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

order  = input("What would you like? Type the name of the drink : latte/espresso/cappuccino  - ").lower()

while order != "off":
    if order == "report":
            coffee_maker.report()
            money.report()
            order  = input("What would you like? Type the name of the drink : latte/espresso/cappuccino  - ").lower()
    elif new_menu.find_drink(order) == "None":
        order = input("You entered an invalid drink. Try again  - ").lower()
    else:
        drink = new_menu.find_drink(order)
        if not coffee_maker.is_resource_sufficient(drink):
            print("Sorry there are not enogh resources for this drink. Try another one.  ")
            order = input("What would you like? Type the name of the drink : latte/espresso/cappuccino  - ").lower()
        elif money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            order = input("What would you like? Type the name of the drink : latte/espresso/cappuccino  - ").lower()
        else:
            order = input("You did not enter enough money for the drink. Select another one and try again.  - ").lower()
