from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    print(menu.get_items()+":", end="")
    user_order = input()

    if user_order == 'report':
        coffee.report()
        money_machine.report()
    elif user_order == 'off':
        exit()
    elif menu.find_drink(user_order) is not None:
        user_order = menu.find_drink(user_order)
        if coffee.is_resource_sufficient(user_order) and money_machine.make_payment(user_order.cost):
            coffee.make_coffee(user_order)

