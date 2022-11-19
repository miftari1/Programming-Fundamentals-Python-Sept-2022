my_dictionary = {}
while True:
    command = input()
    if command == "statistics":
        break
    command_elements = command.split(": ")
    product = command_elements[0]
    quantity = int(command_elements[1])
    if product in my_dictionary.keys():
        my_dictionary[product] += quantity
    else:
        my_dictionary[product] = quantity

print('Products in stock:')
for product, quantity in my_dictionary.items():
    print('-', end=' ')
    print(f'{product}', end=': ')
    print(f'{quantity}')
print(f'Total Products: {len(my_dictionary)}')
print(f'Total Quantity: {sum(my_dictionary.values())}')