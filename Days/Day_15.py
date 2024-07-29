MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(drink, items):
    for ingredient in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][ingredient] > items.get(ingredient, 0):
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def update_money(money, cost):
    money += cost
    return money

def check_payment(quarters, dimes, nickels, pennies, money, cost, drink):
    payment = (quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01)
    if payment < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False, money

    money = update_money(money, cost)

    change = payment - cost
    if change > 0:
        print(f"Here is ${round(change, 2)} in change.")
    print(f"Here is your {drink} ☕️ Enjoy!")
    return True, money

def get_cost(drink):
    return MENU[drink]['cost']

def sale(selection, money, resources):
    if not check_resources(selection, resources):
        return money
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    successful_payment, money = check_payment(quarters, dimes, nickels, pennies, money, get_cost(selection), selection)
    if successful_payment:
        resources = update_resources(resources, selection)
    return money

def update_resources(resources, selection):
    for ingredient in MENU[selection]['ingredients']:
        resources[ingredient] -= MENU[selection]['ingredients'][ingredient]
    return resources

def coffee_machine():
    money = 0
    power = True
    while power:
        user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_prompt == 'report':
            print(f"""
            Water:  {resources['water']}ml
            Milk:   {resources['milk']}ml
            Coffee: {resources['coffee']}g
            Money:  ${money}""")
        elif user_prompt in MENU:
            money = sale(user_prompt, money, resources)
        else:
            print("Sorry, you didn't enter a proper selection.")
        cont = input("Would you like something else? (yes/no): ").lower()
        power = False if cont == 'no' else True
    print("We're closed. Thanks for stopping by!")

coffee_machine()
