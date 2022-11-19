number_sequence_list = input().split()
even_numbers_list = []

# defining the only_even_numbers() function which returns True if the current number in the sequence is even
# and False if the current number is odd


def only_even_numbers(current_number):
    digit = int(current_number)
    if digit % 2 == 0:
        return True
    else:
        return False

# the filter() function implements the code in the only_even_numbers() function
# and filters each number in the numbers sequence


filtered_numbers = filter(only_even_numbers, number_sequence_list)

for number in filtered_numbers:
    even_numbers_list.append(int(number))

print(even_numbers_list)