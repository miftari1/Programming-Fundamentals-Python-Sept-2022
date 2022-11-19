names_list = input().split(", ")
while True:
    command = input()
    current_name = ""
    if command == "Report":
        break
    command_elements = command.split(" ")
    if "Blacklist" in command_elements:
        given_name = command_elements[1]
        if given_name in names_list:
            names_list[names_list.index(given_name)] = "Blacklisted"
            print(f"{given_name} was blacklisted.")
        else:
            print(f"{given_name} was not found.")
    elif "Error" in command_elements:
        index = int(command_elements[1])
        if index in range(len(names_list)) and names_list[index] != "Blacklisted" and names_list[index] != "Lost":
            current_name = names_list[index]
            names_list[index] = "Lost"
            print(f"{current_name} was lost due to an error.")
    elif "Change" in command_elements:
        index = int(command_elements[1])
        replacement_name = command_elements[2]
        if index in range(len(names_list)):
            current_name = names_list[index]
            names_list[index] = replacement_name
            print(f"{current_name} changed his username to {replacement_name}.")
print(f"Blacklisted names: {names_list.count('Blacklisted')}")
print(f"Lost names: {names_list.count('Lost')}")
print(" ".join(names_list))