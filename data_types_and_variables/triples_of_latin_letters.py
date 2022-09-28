number = int(input())
for first_character in range(97, 97 + number):
    for second_character in range(97, 97 + number):
        for third_character in range(97, 97 + number):
            print(f"{chr(first_character)}{chr(second_character)}{chr(third_character)}")