numbers_list = input().split()
numbers_to_remove = int(input())
numbers_list_in_digit = []
for digit in numbers_list:
    numbers_list_in_digit.append(int(digit))
for number in range(numbers_to_remove):
    numbers_list_in_digit.remove(min(numbers_list_in_digit))
i = 1
for current_number in numbers_list_in_digit:
    if i == len(numbers_list_in_digit):
        print(str(current_number))
    else:
        print(str(current_number), end=", ")
    i += 1