budget = float(input())
flour_price = float(input())
colored_eggs = 0
loaf_counter = 0
price_eggs = flour_price * 0.75
price_milk_quarter = (flour_price * 1.25) / 4
cost_a_loaf = flour_price + price_eggs + price_milk_quarter
while budget - cost_a_loaf >= 0:
    budget -= cost_a_loaf
    loaf_counter += 1
    colored_eggs += 3
    if loaf_counter % 3 == 0:
        colored_eggs -= (loaf_counter - 2)
else:
    print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")