list_of_numbers = list(map(int, input().split(" ")))
command = input()
while command != "end":
    command_elements = command.split(" ")
    if "swap" in command_elements:
        first_index = int(command_elements[1])
        second_index = int(command_elements[2])
        list_of_numbers[first_index], list_of_numbers[second_index] = \
            list_of_numbers[second_index], list_of_numbers[first_index]
    elif "multiply" in command_elements:
        first_index = int(command_elements[1])
        second_index = int(command_elements[2])
        list_of_numbers[first_index] = list_of_numbers[first_index] * list_of_numbers[second_index]
    elif "decrease" in command_elements:
        for index in range(len(list_of_numbers)):
            list_of_numbers[index] -= 1
    command = input()
print(", ".join(list(map(str, list_of_numbers))))