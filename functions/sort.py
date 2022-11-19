numbers_list = input().split()
list_of_integers = []
for current_index in range(len(numbers_list)):
    current_digit = int(numbers_list[current_index])
    list_of_integers.append(current_digit)
print(sorted(list_of_integers))