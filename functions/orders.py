product_to_order = input()
product_quantity = int(input())

coffee_price = 1.50
water_price = 1
coke_price = 1.40
snacks_price = 2


def order_price_caltulation(product_choice, quantity):
    price_of_order = None
    if product_choice == "coffee":
        price_of_order = coffee_price * quantity
    elif product_choice == "water":
        price_of_order = water_price * quantity
    elif product_choice == "coke":
        price_of_order = coke_price * quantity
    elif product_choice == "snacks":
        price_of_order = snacks_price * quantity
    return f"{price_of_order:.2f}"


print(order_price_caltulation(product_to_order, product_quantity))

