numbers_sequence = list(map(int, input().split(", ")))
srted = []
current_group = 10
while len(numbers_sequence) > 0:
    lst = list(filter(lambda num: num <= current_group, numbers_sequence))
    for num in lst:
        numbers_sequence.remove(num)
    print(f"Group of {current_group}'s: {lst}")
    current_group += 10