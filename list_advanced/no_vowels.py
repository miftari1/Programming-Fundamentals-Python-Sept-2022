letters_list = list(input())
vowels_list = ["a", "A", "o", "O", "u", "U", "e", "E", "i", "I"]
modified_list = [letter for letter in letters_list if letter not in vowels_list]
print("".join(modified_list))