from math import ceil
number_passengers = int(input())
elevator_capacity = int(input())
courses_needed = ceil(number_passengers / elevator_capacity)
print(courses_needed)