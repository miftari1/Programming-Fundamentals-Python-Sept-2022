first_number = int(input())
second_number = int(input())
third_number = int(input())


def multiplication_sign(first, second, third):
    numbers_list = [first, second, third]
    negative_counter = 0
    for current_number in numbers_list:
        if current_number < 0:
            negative_counter += 1
    if 0 in numbers_list:
        result = "zero"
    elif negative_counter == 0 or negative_counter == 2:
        result = "positive"
    elif negative_counter != 2:
        result = "negative"
    return result


print(multiplication_sign(first_number, second_number, third_number))