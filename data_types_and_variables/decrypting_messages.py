key_number = int(input())
number_of_lines = int(input())
decrypted_message = ""
for character in range(number_of_lines):
    current_character = input()
    decrypted_character = ord(current_character) + key_number
    decrypted_message += chr(decrypted_character)
print(decrypted_message)