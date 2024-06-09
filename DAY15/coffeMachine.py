from requirements import resources
from requirements import MENU

resources = resources
resources["money"] = "$0"


# TODO: Print report.
def ingredients_available():
    for key in resources.keys():
        print(key.capitalize() + ":" + str(resources[key]))


# TODO: Check resources sufficient?
def check_resources(item):
    for key in MENU[item]["ingredients"].keys():
        if resources[key] < MENU[item]["ingredients"][key]:
            print(f"Sorry, There is not enough {key}")
            return False
    return True


# TODO: Process coins
def processing_coins():
    print("Please insert coins:")
    quarters = int(input("How Many no of quarters? "))
    dimes = int(input("How Many no of dimes? "))
    nickles = int(input("How Many no of nickles? "))
    pennies = int(input("How Many no of pennies? "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total


# TODO: Check transaction successful?
def validating_coins(user_input, input_money):
    item_cost = MENU[user_choice]["cost"]
    if item_cost > input_money:
        print("“Sorry that's not enough money. Money refunded.")
        return False
    elif item_cost == input_money:
        money_temp = int(resources["money"].replace("$", ''))
        resources["money"] = money_temp + MENU[user_input]["cost"]
        return True
    else:
        money_temp = float(str(resources["money"]).replace("$", '').strip())
        resources["money"] = money_temp + MENU[user_input]["cost"]
        print(f"Here is ${round(input_money - item_cost, 2)} dollars in change.")
        return True


# TODO: Reducing the resources after dispensing coffee to the user
def make_coffee(user_input):
    resources["water"] = resources["water"] - MENU[user_input]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[user_input]["ingredients"]["coffee"]
    if user_input != "espresso":
        resources["milk"] = resources["milk"] - MENU[user_input]["ingredients"]["milk"]
    return


# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "off":
        exit()
    elif user_choice == "report":
        ingredients_available()
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        if check_resources(user_choice):
            received_money = processing_coins()
            if validating_coins(user_choice, received_money):
                make_coffee(user_choice)
                print(f"Here is your {user_choice}. Enjoy!")
