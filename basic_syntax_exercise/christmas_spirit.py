quantity_to_buy = int(input())
days_until_christmas = int(input())
cost_counter= 0
days_counter = 1
points_counter = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
while days_counter <= days_until_christmas:
    if days_counter % 11 == 0:
        quantity_to_buy += 2
    if days_counter % 2 == 0:
        cost_counter += (quantity_to_buy * ornament_set_price)
        points_counter += 5

    if days_counter % 3 == 0:
        cost_counter += (tree_skirt_price + tree_garland_price) * quantity_to_buy
        points_counter += 13

    if days_counter % 5 == 0:
        cost_counter += (quantity_to_buy * tree_lights_price)
        points_counter += 17
        if days_counter % 3 == 0:
            points_counter += 30

    if days_counter % 10 == 0:
        points_counter -= 20
        cost_counter += tree_skirt_price + tree_garland_price + tree_lights_price
    days_counter += 1
if days_until_christmas == 10 and days_counter == 10:
    points_counter -= 30

print(f"""Total cost: {cost_counter}
Total spirit: {points_counter}
""")