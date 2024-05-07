strings_lst = input().split(' ')
if '' not in strings_lst:
    command = input()
    while command != '3:1':
        command_info = command.split()
        if 'merge' in command_info:
            start_index = int(command_info[1])
            end_index = int(command_info[2])
            if start_index < 0 and end_index >= len(strings_lst):
                strings_lst[:] = [''.join(strings_lst[:])]
            elif start_index < 0 and end_index < len(strings_lst):
                strings_lst[:end_index + 1] = [''.join(strings_lst[:end_index + 1])]
            elif start_index >= 0 and end_index >= len(strings_lst):
                strings_lst[start_index:] = [''.join(strings_lst[start_index:])]
            elif start_index >= 0 and end_index < len(strings_lst):
                strings_lst[start_index:end_index + 1] = [''.join(strings_lst[start_index:end_index + 1])]
        elif 'divide' in command_info:
            element_to_divide_index = int(command_info[1])
            element_to_divide = strings_lst[element_to_divide_index]
            partitions = int(command_info[2])
            if partitions == 0:
                partitions = 1
            substring_lenght = len(element_to_divide) // partitions
            divided_element = []
            if len(element_to_divide) % partitions == 0:
                for i in range(0, len(element_to_divide), substring_lenght):
                    divided_element.append(element_to_divide[i: i + substring_lenght])
            else:
                i = 0
                for _ in range(partitions - 1):
                    divided_element.append(element_to_divide[i: i + substring_lenght])
                    i += substring_lenght
                last_partition = [''.join(element_to_divide[i:])]
                divided_element.extend(last_partition)
            strings_lst[element_to_divide_index:element_to_divide_index + 1] = divided_element[:]
        command = input()
    print(' '.join(strings_lst))