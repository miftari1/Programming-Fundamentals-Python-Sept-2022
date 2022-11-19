list_of_characters = input().split(", ")
dictionary = {character:ord(character) for character in list_of_characters}
print(dictionary)