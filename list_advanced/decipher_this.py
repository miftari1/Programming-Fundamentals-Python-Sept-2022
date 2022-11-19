message = list(map(list, input().split(" ")))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
deciphred_list = []
for word in message:
    ascii_code = ""
    for letter in word:
        if letter not in letters:
            ascii_code += letter
    for letter in ascii_code:
        word.remove(letter)
    word.insert(0, chr(int(ascii_code)))
    word[-1], word[1] = word[1], word[-1]
    word = "".join(word)
    print(word, end=" ")