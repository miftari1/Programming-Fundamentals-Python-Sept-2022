day_events_list = input().split("|")
energy = 100
coins = 100
cannot_afford = False
for event in day_events_list:
    element = event.split("-")
    instruction = element[0]
    if instruction == "rest":
        current_energy = energy
        energy_to_add = int(element[1])
        energy += energy_to_add
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif instruction == "order":
        coins_to_earn = int(element[1])
        if energy >= 30:
            energy -= 30
            coins += coins_to_earn
            print(f"You earned {coins_to_earn} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        ingredient_to_buy = element[0]
        coins_to_spend = int(element[1])
        if coins - coins_to_spend >= 0:
            coins -= coins_to_spend
            print(f"You bought {ingredient_to_buy}.")
        else:
            print(f"Closed! Cannot afford {ingredient_to_buy}.")
            cannot_afford = True
            break
if not cannot_afford:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")