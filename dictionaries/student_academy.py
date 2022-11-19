grades_book = {}
number_of_rows = int(input())
for _ in range(number_of_rows):
    student_name = input()
    grade = float(input())
    if student_name not in grades_book:
        grades_book[student_name] = []
    grades_book[student_name].append(grade)
for student_name in grades_book.keys():
    final_grade = sum(grades_book[student_name]) / len(grades_book[student_name])
    if final_grade >= 4.50:
        print(f'{student_name} -> {final_grade:.2f}')