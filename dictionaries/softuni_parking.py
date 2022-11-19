registered_users = {}
number_of_commands = int(input())
for _ in range(number_of_commands):
    command_elements = input().split(" ")
    username = command_elements[1]
    if "register" in command_elements:
        plate_number = command_elements[2]
        if username in registered_users.keys():
            print(f"ERROR: already registered with plate number {registered_users[username]}")
        else:
            registered_users[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    elif "unregister" in command_elements:
        if username not in registered_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            del registered_users[username]
            print(f"{username} unregistered successfully")
for username in registered_users.keys():
    print(f"{username} => {registered_users[username]}")