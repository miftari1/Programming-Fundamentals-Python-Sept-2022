gifts_names_list = input().split()
command = input()
while command != "No Money":
    listed_command = command.split()
    if "OutOfStock" in listed_command and len(listed_command) == 2:
        current_gift = listed_command[1]
        for index in range(len(gifts_names_list)):
            if gifts_names_list[index] == current_gift:
                gifts_names_list[index] = "None"
    elif "Required" in listed_command and len(listed_command) == 3:
        gift_index = int(listed_command[2])
        current_gift = listed_command[1]
        if gift_index <= len(gifts_names_list) - 1:
            gifts_names_list[gift_index] = listed_command[1]
    elif "JustInCase" in listed_command and len(listed_command) == 2:
        current_gift = listed_command[1]
        gifts_names_list[-1] = current_gift
    command = input()
for element in gifts_names_list:
    if element != "None":
        print(element, end=" ")