word = input()
dictionary = {}
for letter in word:
    if letter == " ":
        continue
    else:
        if letter not in dictionary:
            dictionary[letter] = 0
        dictionary[letter] += 1
for letter, number_of_times in dictionary.items():
    print(f'{letter} -> {number_of_times}')