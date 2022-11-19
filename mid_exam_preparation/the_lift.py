people_waiting = int(input())
no_more_space = False
no_more_people = False
lift = list(map(int, input().split(" ")))
for wagon_number in range(len(lift)):
    while lift[wagon_number] < 4:
        if people_waiting == 0:
            no_more_people = True
            break
        lift[wagon_number] += 1
        people_waiting -= 1
if no_more_people and lift[wagon_number] < 4:
    print('The lift has empty spots!')
    print(" ".join(list(map(str, lift))))
elif people_waiting == 0 and wagon_number == len(lift) - 1:
    print(" ".join(list(map(str, lift))))
else:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(list(map(str, lift))))