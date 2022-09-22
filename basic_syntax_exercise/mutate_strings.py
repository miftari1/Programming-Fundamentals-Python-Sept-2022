first_text = input()
second_text = input()
current_index = 0
old_text = ""
text_lenght = len(first_text)
for i in range(text_lenght):
    new_text = f"{second_text[:current_index + 1]}{first_text[current_index + 1:]}"
    if i == 0:
        old_text = first_text
    if new_text != old_text:
        print(new_text)
    old_text = new_text
    current_index += 1