number_of_lines = int(input())
positive_numbers_list = []
negative_numbers_list = []
for _ in range(number_of_lines):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers_list.append(current_number)
    else:
        negative_numbers_list.append(current_number)
count_positives = len(positive_numbers_list)
sum_of_negatives = sum(negative_numbers_list)

print(f"""{positive_numbers_list}
{negative_numbers_list}
Count of positives: {count_positives}
Sum of negatives: {sum_of_negatives}
""")