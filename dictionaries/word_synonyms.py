count_of_words = int(input())
my_dictionary = {}
for _ in range(count_of_words):
    current_word = input()
    synonym = input()
    if current_word not in my_dictionary.keys():
        my_dictionary[current_word] = []
    my_dictionary[current_word].append(synonym)
for element in my_dictionary.items():
    print(element[0], end=" ")
    print("-", end=" ")
    print(", ".join(element[1]))