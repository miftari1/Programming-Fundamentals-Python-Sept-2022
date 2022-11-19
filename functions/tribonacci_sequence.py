number_range = int(input())
numbers = [1]
for i in range(number_range - 1):
    if len(numbers) <= 3:
        numbers.append(sum(numbers))
    else:
        sum_num = sum(numbers[i:(i-3):-1])
        numbers.append(sum_num)
for num in numbers:
    print(num, end=" ")

