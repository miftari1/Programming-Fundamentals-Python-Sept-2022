names_list = input().split(", ")
names_list.sort()


def word_lenght(word):
    return len(word)


names_list.sort(reverse=True, key=word_lenght)
print(names_list)