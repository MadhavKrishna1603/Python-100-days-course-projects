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
balance = 0


def insert_coin(item_amt, drink):
    print("Please insert coins")
    penny = int(input("penny: $"))
    nikel = int(input("nikel: $"))
    dime = int(input("dimes: $"))
    quater = int(input("quater: $"))
    penny *= 0.01
    nikel *= 0.05
    dime *= 0.1
    quater *= 0.25
    total = penny + nikel + dime + quater
    change = round(total - item_amt, 2)
    if total > item_amt:
        print(f"Here is your drink {drink}☕ and your change ${change}")
    elif total == item_amt:
        print(f"Here is your drink {drink}")
    else:
        print("Sorry you don't have enough money")


game_over = False

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
while not game_over:
    espresso_cost = 1.5
    latte_cost = 2.5
    cappuccino_cost = 3.0

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "espresso":
        balance += espresso_cost
        if MENU["espresso"]["ingredients"]["water"] > water:
            print("There is no sufficiant resources.")
        elif MENU["espresso"]["ingredients"]["coffee"] > coffee:
            print("There is no sufficiant resources.")
        else:
            balance += espresso_cost
            water -= MENU["espresso"]["ingredients"]["water"]
            coffee -= MENU["espresso"]["ingredients"]["coffee"]
            insert_coin(espresso_cost, choice)
    elif choice == "latte":

        if MENU["latte"]["ingredients"]["water"] > water:
            print("There is no sufficiant resources.")
        elif MENU["latte"]["ingredients"]["milk"] > milk:
            print("There is no sufficiant resources.")
        elif MENU["latte"]["ingredients"]["coffee"] > coffee:
            print("There is no sufficiant resources.")
        else:
            balance += latte_cost
            water -= MENU["latte"]["ingredients"]["water"]
            milk -= MENU["latte"]["ingredients"]["milk"]
            coffee -= MENU["latte"]["ingredients"]["coffee"]
            insert_coin(latte_cost, choice)
    elif choice == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] > water:
            print("There is no sufficiant resources.")
        elif MENU["cappuccino"]["ingredients"]["milk"] > milk:
            print("There is no sufficiant resources.")
        elif MENU["cappuccino"]["ingredients"]["coffee"] > coffee:
            print("There is no sufficiant resources.")
        else:
            balance += cappuccino_cost
            water -= MENU["cappuccino"]["ingredients"]["water"]
            milk -= MENU["cappuccino"]["ingredients"]["milk"]
            coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
            insert_coin(cappuccino_cost, choice)
    elif choice == "report":
        print(f"Water: {water}\nMilk: {milk}\nCoffe: {coffee}\nMoney: {balance}")
    elif choice == "off":
        game_over = True
