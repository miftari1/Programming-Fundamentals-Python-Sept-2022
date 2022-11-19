input_type = input()


def data_type(current_input):
    result = None
    if current_input == "int":
        integer_number = int(input())
        result = integer_number * 2
    elif current_input == "real":
        real_number = float(input())
        multiplication = real_number * 1.5
        result = f"{multiplication:.2f}"
    elif current_input == "string":
        text = input()
        result = f"${text}$"
    return result


print(data_type(input_type))