from replit import clear
from resources import resources,menu

def resource_check(order_drink):
    for item in order_drink:
        if(order_drink[item]>=resources[item]):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def cal_coins():
    print("Please insert coins.")
    total=int(input("How many quarters? : "))*0.25
    total+=int(input("How many dimes? : "))*0.1
    total+=int(input("How many nickles? : "))*0.05
    total+=int(input("How many pennies? : "))*0.01
    return total

def trans_check(money_rec,drink_cost):
    if(money_rec>=drink_cost):
        change=round(money_rec-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False
def make_coffee(drink_name,order_drink):
    for item in order_drink:
        resources[item]-=order_drink[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

again_var=True
profit=0

while again_var:

    user_input=input("What would you like ? (Espresso/Latte/Cappuccino) or Exit : ").lower().strip()

    if(user_input=='report'):
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    elif(user_input=='exit'):
        again_var=False
        clear()
        print("Thank You!")
    elif(user_input=="espresso"):
        drink=menu[user_input]
        if(resource_check(drink['ingredients'])):
            payment=cal_coins()
            if(trans_check(payment,drink['cost'])):
                make_coffee(user_input,drink['ingredients'])
    elif(user_input=="latte"):
        drink=menu[user_input]
        if(resource_check(drink['ingredients'])):
            payment=cal_coins()
            if(trans_check(payment,drink['cost'])):
                make_coffee(user_input,drink['ingredients'])
    elif(user_input=="cappuccino"):
        drink=menu[user_input]
        if(resource_check(drink['ingredients'])):
            payment=cal_coins()
            if(trans_check(payment,drink['cost'])):
                make_coffee(user_input,drink['ingredients'])
    else:
        print("Invalid command! Maybe check spelling.")