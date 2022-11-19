chat_list = []
pinned_message = False
while True:
    command = input()
    if command == "end":
        break
    command_elements = command.split(" ")
    if "Chat" in command_elements:
        current_message = command_elements[1]
        chat_list.append(current_message)
    elif "Delete" in command_elements:
        message_to_delete = command_elements[1]
        if message_to_delete in chat_list:
            chat_list.remove(message_to_delete)
    elif "Edit" in command_elements:
        message_to_edit = command_elements[1]
        edited_message = command_elements[2]
        if message_to_edit in chat_list:
            chat_list[chat_list.index(message_to_edit)] = edited_message
    elif "Pin" in command_elements:
        pinned_message = True
        message_to_pin = command_elements[1]
        if message_to_pin in chat_list:
            chat_list.append(message_to_pin)
            chat_list.remove(message_to_pin)
    elif "Spam" in command_elements:
        messages_to_add = command_elements[1::]
        chat_list.extend(messages_to_add)
for message in chat_list:
    print(message)