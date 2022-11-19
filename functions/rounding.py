numbers_sequence = input().split()
rounded_numbers = []
for current_index in range(len(numbers_sequence)):
    current_digit = float(numbers_sequence[current_index])
    rounded_digit = round(current_digit)
    rounded_numbers.append(rounded_digit)
print(rounded_numbers)