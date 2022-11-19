password = input()


def password_validation(given_password):
    numbers_index_range = range(48, 57 + 1)
    uppercase_letters_index_range = range(65, 90 + 1)
    lowercase_letters_index_range = range(97, 122 + 1)
    is_in_range = False
    valid_symbols = False
    two_digits_included = False
    if 6 <= len(given_password) <= 10:
        is_in_range = True
    else:
        print("Password must be between 6 and 10 characters")
    for letter in given_password:
        if ord(letter) in range(48, 57 + 1) or ord(letter) in range(65, 90 + 1)\
            or ord(letter) in range(97, 122 + 1):
            valid_symbols = True
        else:
            valid_symbols = False
            print("Password must consist only of letters and digits")
            break
    digits_counter = 0
    for current_symbol in given_password:
        if ord(current_symbol) in range(48, 57 + 1):
            digits_counter += 1
    if digits_counter >= 2:
        two_digits_included = True
    else:
        print(f"Password must have at least 2 digits")

    if is_in_range and valid_symbols and two_digits_included:
        print("Password is valid")


password_validation(password)