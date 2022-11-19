numbers_sequence = list(map(int, input().split(" ")))


def above_average_value(lst):
    average_value = sum(lst) / len(lst)
    above_average = sorted([num for num in lst if num > average_value ], reverse=True)
    if len(above_average) >= 5:
        top_five = [above_average[index] for index in range(5)]
    else:
        top_five = [num for num in above_average]
    return top_five


if len(above_average_value(numbers_sequence)) != 0:
    print(" ".join(list(map(str, above_average_value(numbers_sequence)))))
else:
    print('No')