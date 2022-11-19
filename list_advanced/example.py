dictionary = {'numbers': [1, 2, 5]}
for key in dictionary.keys():
    for index in range(len(dictionary[key])):
        if dictionary[key][index] == 5:
            del dictionary[key][index]
            break
print(dictionary)
