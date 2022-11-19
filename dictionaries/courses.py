courses= {}
while True:
    input_line = input()
    if input_line == "end":
        break
    elements = input_line.split(" : ")
    course_name = elements[0]
    student = elements[1]
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(f'-- {student}')
for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f'{student}')