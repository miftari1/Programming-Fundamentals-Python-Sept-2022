even_lenght_words = [word for word in input().split(" ") if len(word) % 2 == 0]
for word in even_lenght_words:
    print(word)