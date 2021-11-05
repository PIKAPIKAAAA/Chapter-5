current_users = ['Pika', 'Dolarichi', 'Papito', 'Bobicha', 'Giosha']
new_users = ['KRIGERA', 'Dolarichi', 'papito', 'Marusa', 'klausi']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'The username "{new_user}" is not available, please choose other.')
    else:
        print(f'Username {new_user} is available.')