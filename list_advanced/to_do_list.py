to_do_list = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    elements_command = command.split("-")
    task_importance = int(elements_command[0]) - 1
    current_task = elements_command[1]
    to_do_list.pop(task_importance)
    to_do_list.insert(task_importance, current_task)
final_list = [element for element in to_do_list if element != 0]
print(final_list)