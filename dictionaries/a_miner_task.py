COMMAND_STOP = "stop"
resources_dictionary = {}
resource = input()
while resource != COMMAND_STOP:
    quantity = int(input())
    if resource not in resources_dictionary:
        resources_dictionary[resource] = 0
    resources_dictionary[resource] += quantity
    resource = input()
for resource, quantity in resources_dictionary.items():
    print(f'{resource} -> {quantity}')