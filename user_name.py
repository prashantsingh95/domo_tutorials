while True:
    name = input('Enter your name :- ')
    if name != 'hello':
        continue
    password = input('Enter ur Password :- ')
    if password == '123':
        break
print('Access Granted')
