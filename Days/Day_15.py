import pandas as pd

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


# TODO: 1. Print report of all coffee machine resources.

def check_resources(drink, resources):
    if drink[ingredients][water] > resources[water]:
        print("Sorry there is not enough water.")
        return
    elif drink[ingredients][milk] > resources[milk]:
        print("Sorry there is not enough milk.")
        return
    elif drink[ingredients][coffee] > resources[coffee]:
        print("Sorry there is not enough coffee.")
        return

def check_payment(quarters, dimes, nickles, pennies, money, cost, drink, emoji):
    payment = (quarters*25 + dimes*10 + nickles*5 + pennies) / 100
    if payment < cost:
        print("Sorry that's not enough money. Money refunded")
        return
    change = payment - cost
    money += cost
    if change > 0:
        print(f"Here is ${change} in change.")
    print(f"Here is your {drink}  Enjoy!") # Enter emoji from keyboard

def coffee_machine():
    money = 0
    user_prompt = input("What would you like? (espresso/latte/capuccino): ")
    if user_prompt[0] == 'r':
        print(f"""
        Water:  {resources[water]}ml
        Milk:   {resources[milk]}ml
        Coffee: {resouces[coffee]}g
        Money:  ${money}""")






