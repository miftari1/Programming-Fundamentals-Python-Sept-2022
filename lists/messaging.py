numbers_sequence_list = input().split()
text = input()
list_of_text_chars = []
message = ""
for char in text:
    list_of_text_chars.append(char)
for numbers_set in numbers_sequence_list:
    digit_list = []
    for digit in numbers_set:
        digit_list.append(int(digit))
    sum_digits = sum(digit_list)
    for letter_index in range(len(list_of_text_chars)):
        if sum_digits >= len(list_of_text_chars):
            sum_digits -= len(list_of_text_chars)
        if letter_index == sum_digits:
            message += list_of_text_chars[letter_index]
            list_of_text_chars.remove(list_of_text_chars[letter_index])
print(message)
