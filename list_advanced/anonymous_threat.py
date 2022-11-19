strings_array = input().split(" ")
if "" not in strings_array:
    while True:
        command = input()
        if command == "3:1":
            break
        instructions_list = command.split(" ")
        if "merge" in instructions_list:
            start_index = int(instructions_list[1])
            end_index = int(instructions_list[2])
            if start_index < 0:
                start_index = 0
            if end_index >= len(strings_array):
                end_index = len(strings_array)
            strings_array[start_index] = "".join(strings_array[start_index:end_index])
            for i in range(end_index, start_index, -1):
                strings_array.pop(i)
        elif "divide" in instructions_list:
            pass
print(strings_array)