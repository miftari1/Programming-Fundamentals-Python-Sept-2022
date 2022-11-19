elements_sequence = input().split(" ")
have_won = False
moves = 0
current_indexes = input()
while current_indexes != "end":
    moves += 1
    current_indexes = current_indexes.split(" ")
    first_index = int(current_indexes[0])
    second_index = int(current_indexes[1])
    if first_index == second_index or first_index not in range(len(elements_sequence))\
            or second_index not in range(len(elements_sequence)):
        for i in range(2):
            elements_sequence.insert(len(elements_sequence)// 2, f"-{moves}a")
        print('Invalid input! Adding additional elements to the board')
        current_indexes = input()
        continue
    if elements_sequence[first_index] == elements_sequence[second_index]:
        element_to_remove = elements_sequence[first_index]
        while element_to_remove in elements_sequence:
            for element in elements_sequence:
                if element == element_to_remove:
                    elements_sequence.remove(element)
        print(f"Congrats! You have found matching elements - {element_to_remove}!")
    elif elements_sequence[first_index] != elements_sequence[second_index]:
        print('Try again!')
    for element_index in range(len(elements_sequence)):
        if elements_sequence.count(elements_sequence[element_index]) != 2:
            have_won = True
            break
    if len(elements_sequence) == 0:
        have_won = True
        break
    if have_won:
        break
    current_indexes = input()
if have_won:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(")
    print(" ".join(elements_sequence))