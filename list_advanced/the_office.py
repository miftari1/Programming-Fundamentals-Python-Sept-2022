employees = list(map(int, input().split(" ")))
factor = int(input())

improved_happiness = list(map(lambda x: x * factor, employees))

happy_employees = list(filter(
    lambda current_employee_happiness: current_employee_happiness >=\
                                       (sum(improved_happiness) / len(improved_happiness)), improved_happiness)
)

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")