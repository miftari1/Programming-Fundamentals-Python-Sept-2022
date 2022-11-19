items_to_buy = input().split("|")
bought_items = []
total_cost_items = 0
budget = float(input())
for item in items_to_buy:
    item_elements = item.split("->")
    item_type = item_elements[0]
    item_price = float(item_elements[1])
    if item_type == "Clothes" and item_price <= 50:
        if budget - item_price >= 0:
            budget -= item_price
            bought_items.append(item_price)
    elif item_type == "Shoes" and item_price <= 35:
        if budget - item_price >= 0:
            budget -= item_price
            bought_items.append(item_price)
    elif item_type == "Accessories" and item_price <= 20.50:
        if budget - item_price >= 0:
            budget -= item_price
            bought_items.append(item_price)
for value in bought_items:
    value += 0.40 * value
    budget += value
    print(f"{value:.2f}", end=" ")
print()
profit = sum(bought_items) - 0.60 * (sum(bought_items))
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')