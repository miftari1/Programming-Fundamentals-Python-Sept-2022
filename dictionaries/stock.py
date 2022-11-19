elements = input().split(" ")
products_to_search = input().split(" ")
my_dictionary = {}
for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    my_dictionary[key] = value
for product in products_to_search:
    if product in my_dictionary.keys():
        print(f'We have {my_dictionary[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')