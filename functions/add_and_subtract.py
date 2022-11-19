first_number = int(input())
second_number = int(input())
third_number = int(input())


def add_and_subtract(first, second, third):
    # defining the sum_numbers() function which returns the sum of the first two integers
    def sum_numbers():
        sum_of_first_two = first + second
        return sum_of_first_two

    # defining the subtract() function which returns the result of subtracting
    # the third integer from the sum of the first two
    def subtract():
        result_subtraction = sum_numbers() - third
        return result_subtraction

    return subtract()


print(add_and_subtract(first_number, second_number, third_number))
