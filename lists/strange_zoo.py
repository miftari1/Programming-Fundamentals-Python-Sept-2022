body_list = []
for i in range(3):
    body_part = input()
    body_list.append(body_part)
body_list[0], body_list[2] = body_list[2], body_list[0]
print(body_list)
