employees_efficiency = [int(input()) for _ in range(3)]
number_students = int(input())
hours_counter = 0
while number_students != 0:
    hours_counter += 1
    if hours_counter % 4 != 0:
        if number_students - sum(employees_efficiency) < 0:
            number_students -= number_students
            break
        number_students -= sum(employees_efficiency)
print(f"Time needed: {hours_counter}h.")