first_number = int(input())
second_number = int(input())


def factorial_division(x, y):
    factorial_of_x = 1
    factorial_of_y = 1
    for current_integer_in_x in range(1, x + 1):
        factorial_of_x *= current_integer_in_x
    for current_integer_in_y in range(1, y + 1):
        factorial_of_y *= current_integer_in_y
    division_result = factorial_of_x / factorial_of_y
    return f"{division_result:.2f}"


print(factorial_division(first_number, second_number))