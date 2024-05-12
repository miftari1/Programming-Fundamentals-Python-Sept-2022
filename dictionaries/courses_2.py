def update_course_list(course, student):
    """Updates the course list with new courses and new students."""
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(student)


def show_courses():
    """Shows the information about each course and it's participants in the needed format"""
    for course, students in courses.items():
        number_students = len(students)
        print(f'{course}: {number_students}')
        for student in students:
            print(f'-- {student}')


courses = dict()
info = input().split(' : ')
while 'end' not in info:
    course_name = info[0]
    student_name = info[1]
    update_course_list(course_name, student_name)
    info = input().split(' : ')

show_courses()
