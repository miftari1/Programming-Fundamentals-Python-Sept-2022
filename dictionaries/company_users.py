companies = {}
command = input()
while command != "End":
    command_elements = command.split(" -> ")
    company_name = command_elements[0]
    employee_id = f'-- {command_elements[1]}'
    if company_name not in companies:
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)
    command = input()
for company_name, employees in companies.items():
    print(f'{company_name}')
    for employee_id in employees:
        print(employee_id)