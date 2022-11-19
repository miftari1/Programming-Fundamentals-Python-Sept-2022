number = int(input())


def perfect_number(num):
    valid_divisors = []
    for num_divisor in range(1, num):
        if num % num_divisor == 0:
            valid_divisors.append(num_divisor)
    if sum(valid_divisors) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(number)