encrypted_message = list(input())
current_instruction = input()
while current_instruction != "Decode":
    instruction_elements = current_instruction.split("|")
    if "Move" in instruction_elements:
        number_letters = int(instruction_elements[1])
        for index_to_move in range(number_letters):
            encrypted_message.append(encrypted_message[index_to_move])
        for index_to_remove in range((number_letters - 1), -1, -1):
            encrypted_message.pop(index_to_remove)
    elif "Insert" in instruction_elements:
        index_to_insert = int(instruction_elements[1])
        value_to_insert = instruction_elements[2]
        encrypted_message.insert(index_to_insert, value_to_insert)
    elif "ChangeAll" in instruction_elements:
        value_to_change = instruction_elements[1]
        replacement_value = instruction_elements[2]
        for index in range(len(encrypted_message)):
            if encrypted_message[index] == value_to_change:
                encrypted_message[index] = replacement_value
    current_instruction = input()
print(f'The decrypted message is: {"".join(encrypted_message)}')