input_number = input()

# defining the sum_even_odd_digits() function which returns
# the sums of all even and all odd digits in a given number


def sum_even_odd_digits(number):
    sum_even_digits = 0
    sum_odd_digits = 0
    digit_list = list(number)
    for current_index in range(len(digit_list)):
        current_digit = int(digit_list[current_index])
        if current_digit % 2 == 0:
            sum_even_digits += current_digit
        else:
            sum_odd_digits += current_digit

    conclusion = f"Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}"
    return conclusion


print(sum_even_odd_digits(input_number))


