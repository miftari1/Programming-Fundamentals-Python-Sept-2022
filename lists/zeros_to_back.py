numbers_list = input().split(", ")
for number in numbers_list:
    if number == "0":
        numbers_list.remove(number)
        numbers_list.append(number)
for index in range(len(numbers_list)):
    numbers_list[index] = int(numbers_list[index])
print(numbers_list)