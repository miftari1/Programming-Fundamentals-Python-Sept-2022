electrons = int(input())
current_shell = 1
shells_list= []
while electrons != 0:
    current_number_electrons = 2 * current_shell ** 2
    if electrons - current_number_electrons < 0:
        shells_list.append(electrons)
        break
    else:
        shells_list.append(current_number_electrons)
        electrons -= shells_list[current_shell - 1]
        current_shell += 1
print(shells_list)

