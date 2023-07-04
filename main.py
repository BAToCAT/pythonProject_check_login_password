
user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

# username = input()
# password = input()

def check_user(username, password):
    if username in user_database:
        if password == user_database[username]:
            return True
        else:
            return False
    else:
        return False

# print(check_user(username = 'user', password = 'password'))
# print(check_user(username = '1user', password = 'password'))
# print(check_user(username = 'user', password = 'passwordd'))
# print(check_user(username, password))