number_losses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmets = number_losses // 2
broken_swords = number_losses // 3
broken_shields = number_losses // 6
broken_armors = broken_shields // 2
cost_to_renew_equipment = broken_helmets * helmet_price + \
    broken_swords * sword_price + \
    broken_shields * shield_price + \
    broken_armors * armor_price
print(f"Gladiator expenses: {cost_to_renew_equipment:.2f} aureus")