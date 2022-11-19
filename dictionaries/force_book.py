sides_and_users = {}
while True:
    input_line = input()
    if input_line == "Lumpawaroo":
        break
    if "|" in input_line:
        info = input_line.split(" | ")
        force_side = info[0]
        user = info[1]
        if force_side not in sides_and_users.keys():
            sides_and_users[force_side] = []
            in_users = False
        for users in sides_and_users.values():
            if user in users:
                in_users = True
                break
        if not in_users:
            sides_and_users[force_side].append(user)
    elif " -> " in input_line:
        info = input_line.split(" -> ")
        user = info[0]
        force_side = info[1]
        if force_side not in sides_and_users.keys():
            sides_and_users[force_side] = []
        for key in sides_and_users.keys():
            for index in range(len(sides_and_users[key])):
                if sides_and_users[key][index] == user:
                    del sides_and_users[key][index]
        sides_and_users[force_side].append(user)
        print(f'{user} joins the {force_side} side!')
for force_side in sides_and_users.keys():
    if len(sides_and_users[force_side]) > 0:
        print(f'Side: {force_side}, Members: {len(sides_and_users[force_side])}')
        for user in sides_and_users[force_side]:
            print(f'! {user}')