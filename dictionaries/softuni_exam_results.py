submissions_counter = 0
exam_results = {}
submissions = {}
while True:
    line = input().split("-")
    if len(line) <= 1:
        break
    if "banned" in line:
        user_to_ban = line[0]
        for key in exam_results.keys():
            if user_to_ban in exam_results[key]:
                del exam_results[key][user_to_ban]
    else:
        username = line[0]
        language = line[1]
        points = int(line[2])
        if language not in exam_results.keys():
            exam_results[language] = {}
            submissions[language] = 0
        submissions[language] += 1
        if username not in exam_results[language]:
            exam_results[language][username] = points
        if points > exam_results[language][username]:
            exam_results[language][username] = points
print('Results:')
for participants in exam_results.values():
    for key, value in participants.items():
        print(f'{key} | {value}')
print('Submissions:')
for key, value in submissions.items():
    print(f'{key} - {value}')





