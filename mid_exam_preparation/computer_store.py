command = input()

parts_prices_list = []
total_tax = 0
while command != "special" and command != "regular":
    if float(command) < 0:
        print('Invalid price!')
    else:
        parts_prices_list.append(float(command))
    command = input()
for current_price in parts_prices_list:
    if current_price < 0:
        continue
    else:
        total_tax += current_price * 0.2
price_without_tax = sum(parts_prices_list)
total_price = price_without_tax + total_tax
if total_price == 0:
    print('Invalid order!')
else:
    if command == "special":
        total_price = total_price * 0.9
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {price_without_tax:.2f}$
Taxes: {total_tax:.2f}$
-----------
Total price: {total_price:.2f}$
""")