def user_register(name, plate):
    """Registers a new user and it's car plate."""
    if name in registered_users.keys():
        return f'ERROR: already registered with plate number {registered_users[name]}'
    registered_users[name] = plate
    return f'{name} registered {plate} successfully'


def remove_user(name):
    """Removes given user."""
    if name not in registered_users.keys():
        return f'ERROR: user {name} not found'
    registered_users.pop(name)
    return f'{name} unregistered successfully'


def show_users():
    """Shows all currently registered members in the needed format."""
    for user, plate in registered_users.items():
        print(f'{user} => {plate}')


registered_users = dict()
n = int(input())

for _ in range(n):
    command = input().split()
    if 'register' in command:
        username = command[1]
        license_plate = command[2]
        print(user_register(username, license_plate))
    else:
        username = command[1]
        print(remove_user(username))

show_users()
