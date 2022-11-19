text = input()
numbers_list = text.split()
opposite_numbers = []
for number in numbers_list:
    number = -int(number)
    opposite_numbers.append(number)
print(opposite_numbers)
