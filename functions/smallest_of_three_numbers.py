first_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest_of_three(first, second, third):
    smallest = min(first, second, third)
    return smallest


print(smallest_of_three(first_number, second_number, third_number))