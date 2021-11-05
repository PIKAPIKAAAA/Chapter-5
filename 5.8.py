usernames = ['Pika', 'Dolarichi', 'Papito', 'Bobicha', 'Giosha']

for user in usernames:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user}')