COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

number_of_lines = int(input())
numbers_list = []
for _ in range(number_of_lines):
    current_number = int(input())
    numbers_list.append(current_number)

command = input()
filtered_list = []
for number in numbers_list:
    filtered_passes = (
        (command == COMMAND_EVEN and number % 2 == 0 ) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_NEGATIVE and number < 0) or
        (command == COMMAND_POSITIVE and number >= 0)
    )
    if filtered_passes:
        filtered_list.append(number)
print(filtered_list)
