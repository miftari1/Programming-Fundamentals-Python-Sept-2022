number_of_lines = int(input())
key_word = input()
text_list = []
for _ in range(number_of_lines):
    current_text = input()
    text_list.append(current_text)
filtered_list = []
for text in text_list:
    if key_word in text:
        filtered_list.append(text)
print(text_list)
print(filtered_list)