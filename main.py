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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_sufficient(order_ingredients):
    """return true when order can be made and false if insufficient enough resources"""
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def process_coins():
    """returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.10
    total += int(input("how many nickels? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


def transactions_successful(money_collected, drink_cost):
    """return true when payment is successful, or return false if money is insufficient."""
    if money_collected >= drink_cost:
        global profit
        change = round(money_collected - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredient):
    """Deduct the required ingredient from the resources."""
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]
    print(f"Here is your {drink_name} ☕")


is_on = True

# TODO #1: prompt the user by asking "what would you like?"
while is_on:
    user_choice = input("What would you like? (Espresso/Latte/Cappuccino): ")
    #TODO #2:
    if user_choice == 'off':
        is_on = False
    # TODO #3: Print report.
    elif user_choice == "report":
        print(f"water:{resources['water']} Ml")
        print(f"milk:{resources['milk']} Ml")
        print(f"coffee:{resources['coffee']} g")
        print(f"Money:${profit} ")
    # TODO #4: Check resources sufficient?
    else:
        beverage = MENU[user_choice]
        #print(beverage)
        if resources_sufficient(beverage["ingredients"]):
            payment = process_coins()
            if transactions_successful(payment, beverage["cost"]):
                make_coffee(user_choice, beverage["ingredients"])
