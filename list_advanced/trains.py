number_wagons = int(input())
train_list = [0 for wagon in range(number_wagons)]

command = input()
while command != "End":
    command_elements = command.split(" ")
    if "add" in command:
        number_to_add = int(command_elements[1])
        train_list[-1] += number_to_add
    elif "insert" in command:
        wagon_index = int(command_elements[1])
        number_to_add = int(command_elements[2])
        train_list[wagon_index] += number_to_add
    elif "leave" in command:
        wagon_index = int(command_elements[1])
        number_to_remove = int(command_elements[2])
        train_list[wagon_index] -= number_to_remove
    command = input()
print(train_list)