products = {}
while True:
    line_input = input()
    if line_input == "buy":
        break
    elements = line_input.split(" ")
    product_name = elements[0]
    price = float(elements[1])
    quantity = int(elements[2])
    if product_name not in products.keys():
        products[product_name] = [price, quantity]
    else:
        products[product_name][0] = price
        products[product_name][1] += quantity
for key, value in products.items():
    total_price = value[0] * value[1]
    print(f'{key} -> {total_price:.2f}')