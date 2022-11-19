elements_sequence = input().split(" ")
my_dictionary = {}
for word in elements_sequence:
    if word.lower() in my_dictionary.keys():
        my_dictionary[word.lower()] += 1
    else:
        my_dictionary[word.lower()] = 1
for current_key, number_of_times in my_dictionary.items():
    if number_of_times % 2 != 0:
        print(current_key, end=" ")