number_of_rooms = int(input())
free_chairs = 0
total_needed = 0
for current_room in range(1, number_of_rooms + 1):
    room_info = input().split(" ")
    chairs_number = len(list(room_info[0]))
    visitors = int(room_info[1])
    if visitors > chairs_number:
        needed_chairs = visitors - chairs_number
        total_needed += needed_chairs
        print(f"{needed_chairs} more chairs needed in room {current_room}")
    else:
        free_chairs += chairs_number - visitors
if total_needed <= free_chairs:
    print(f"Game On, {free_chairs - total_needed} free chairs left")