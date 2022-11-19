numbers_list = input().split()
absolute_values = []
for index in range(len(numbers_list)):
    digit = abs(float(numbers_list[index]))
    absolute_values.append(digit)
print(absolute_values)

