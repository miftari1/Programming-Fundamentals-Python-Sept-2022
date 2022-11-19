first_sequence = list(map(list, input().split(", ")))
second_sequence = list(map(list, input().split(", ")))
matched_words = []
for i in range(len(first_sequence)):
    for j in range(len(second_sequence)):
        matched_letters = 0
        for letter in first_sequence[i]:
            if letter in second_sequence[j]:
                matched_letters += 1
        if matched_letters == len(first_sequence[i]):
            if "".join(first_sequence[i]) in matched_words:
                continue
            else:
                matched_words.append("".join(first_sequence[i]))
print(matched_words)