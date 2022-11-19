numbers_list = list(map(int, input().split(", ")))

found_indices_or_no = map(
    lambda index: index if numbers_list[index] % 2 == 0 else 'no', range(len(numbers_list))
)

even_numbers_indices = list(filter(lambda even_indice: even_indice != 'no', found_indices_or_no ))
print(even_numbers_indices)