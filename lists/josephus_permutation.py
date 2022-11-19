people = input().split()
step_execution = int(input())
executed_people = []
current_index = 0
for man in people:
    people[current_index] = int(man)
    current_index += 1
step = 1
while len(people) != 0:
    for current_execution in people:
        if step == step_execution:
            executed_people.append(current_execution)
            people.remove(current_execution)
            step = 1
        step += 1

print(executed_people)

