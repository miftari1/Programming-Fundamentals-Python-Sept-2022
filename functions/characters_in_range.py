first_character = input()
second_character = input()

# defining the string_of_characters() function which returns a string
# with all the characters between the two given by the user


def string_of_characters(symbol_one, symbol_two):
    characters_sequence = ""
    for current_index in range(ord(symbol_one) + 1, ord(symbol_two)):
        characters_sequence += f"{chr(current_index)} "

    return characters_sequence


print(string_of_characters(first_character, second_character))