number_inputs = int(input())
total_sum = 0
for character in range(number_inputs):
    character = input()
    total_sum += ord(character)
print(f"The sum equals: {total_sum}")