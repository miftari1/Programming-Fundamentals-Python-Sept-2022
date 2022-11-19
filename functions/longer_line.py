first_line_values = []
second_line_values = []

for user_input in range(8):
    if len(first_line_values) < 4:
        first_line_values.append(float(input()))
    else:
        second_line_values.append(float(input()))


def longer_line(first_list, second_list):
    from math import floor
    lenght_first_line = sum(first_line_values[0:2]) - sum(first_line_values[2:3 + 1])
    lenght_second_line = sum(second_line_values[0:2]) - sum(second_line_values[2:3 + 1])
    if abs(lenght_first_line) >= abs(lenght_second_line):
        if abs(first_line_values[0]) + abs(first_line_values[1]) <= \
                abs(first_line_values[2]) + abs(first_line_values[3]):
            result = f"({floor(first_line_values[0])}, {floor(first_line_values[1])})" \
                     f"({floor(first_line_values[2])}, {floor(first_line_values[3])})"
        else:
            result = f"({floor(first_line_values[2])}, {floor(first_line_values[3])})" \
                     f"({floor(first_line_values[0])}, {floor(first_line_values[1])})"
    else:
        if abs(second_line_values[0]) + abs(second_line_values[1]) <= \
                abs(second_line_values[2]) + abs(second_line_values[3]):
            result = f"({floor(second_line_values[0])}, {floor(second_line_values[1])})" \
                     f"({floor(second_line_values[2])}, {floor(second_line_values[3])})"
        else:
            result = f"({floor(second_line_values[2])}, {floor(second_line_values[3])})"\
                     f"({floor(second_line_values[0])}, {floor(second_line_values[1])})"
    return result


print(longer_line(first_line_values, second_line_values))
