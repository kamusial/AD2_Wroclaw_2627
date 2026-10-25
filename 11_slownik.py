users = {
    'admin': 'admin1',
    'max01': 'XDXD',
    'Kasia76': 'jednorozec',
}

print(users['max01'])
users['Kuba76'] = 'jednorozec'   # dodaje użytkownika
users['Kasia76'] = 'dwunorozec'  # zmieniam hasło
print(users)

print('\nProgram start')
username = input('Enter your username: ')
userpassword = input('Enter your password: ')
if users[username] == userpassword:
    print('Witamy w programie')




