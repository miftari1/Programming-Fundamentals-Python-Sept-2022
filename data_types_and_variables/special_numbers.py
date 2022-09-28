n = int(input())
for num in range(1, n + 1):
    sum_digits = 0
    for digit in str(num):
        sum_digits += int(digit)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        result = f"{num} -> True"
    else:
        result = f"{num} -> False"
    print(result)