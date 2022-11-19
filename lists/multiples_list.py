factor_number = int(input())
count_number = int(input())
multiples_list = []
for number in range(1, count_number + 1):
    current_number = factor_number * number
    multiples_list.append(current_number)
print(multiples_list)