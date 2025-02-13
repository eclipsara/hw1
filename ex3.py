user = input('Enter username: ')
pswd = input('Enter password: ')

if user == 'admin' and pswd == '1234':
    print('Access granted')
else:
    print('Access denied')