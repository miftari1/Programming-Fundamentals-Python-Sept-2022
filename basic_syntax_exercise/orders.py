number_orders = int(input())
total_price_order = 0
for _ in range(number_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not 0.01 <= price_per_capsule <= 100 or not 1 <= days <= 31 or not 1 <= capsules_per_day <= 2000:
        continue
    else:
        current_order = price_per_capsule * days * capsules_per_day
        print(f"The price for the coffee is: ${current_order:.2f}")
        total_price_order += current_order
print(f"Total: ${total_price_order:.2f}")