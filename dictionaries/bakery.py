food_info = input().split(" ")
dictionary = {}
for index in range(0, len(food_info), 2):
    key = food_info[index]
    value = int(food_info[index + 1])
    dictionary[key] = value
print(dictionary)