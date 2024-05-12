def adding_product(name, price, quantity):
    """Adds a product to the dictionary if it doesn't exist."""

    products[name] = [price, quantity]


def product_modify(name, price, quantity):
    """Modifies an already existing product."""

    if products[name][0] != price:
        products[name][0] = price
    products[name][1] += quantity


def show_products(products_dict):
    """Outputs given dictionary in the needed format. """

    for name, info in products_dict.items():
        total_price = info[0] * info[1]
        print(f'{name} -> {total_price:.2f}')


products = dict()
product_info = input()

while product_info != 'buy':
    product_name = product_info.split()[0]
    product_price = float(product_info.split()[1])
    product_quantity = int(product_info.split()[2])

    if product_name not in products:
        adding_product(product_name, product_price, product_quantity)
    else:
        product_modify(product_name, product_price, product_quantity)

    product_info = input()

show_products(products)
