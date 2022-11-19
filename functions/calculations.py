math_operator = input()
first_number = int(input())
second_number = int(input())


def calculation(a, b, operation):
    result = None
    if operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = int(a / b)
    elif operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    return result


print(calculation(first_number, second_number, math_operator))