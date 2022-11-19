numbers = input().split(", ")


def palindrome_check(numbers_list):
    for current_number in numbers_list:
        reversed_number = current_number[::-1]
        if current_number == reversed_number:
            print(True)
        else:
             print(False)


palindrome_check(numbers)