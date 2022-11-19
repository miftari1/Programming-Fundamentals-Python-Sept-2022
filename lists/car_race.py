times_list = input().split()
finish_line = len(times_list) // 2 + 1
time_left_racer = 0
time_right_racer = 0
for index_left in range(finish_line - 1):
    if times_list[index_left] == "0":
        time_left_racer *= 0.8
    time_left_racer += int(times_list[index_left])
for index_right in range(1, finish_line):
    if times_list[-index_right] == "0":
        time_right_racer *= 0.8
    time_right_racer += int(times_list[-index_right])
if time_left_racer < time_right_racer:
    print(f"The winner is left with total time: {time_left_racer:.1f}")
else:
    print(f"The winner is right with total time: {time_right_racer:.1f}")