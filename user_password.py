while True:
    name = input('Enter your name :- ')
    password = input('Enter ur Password :- ')
    if name == 'hello' and password == '123':
        break
    else:
        print('User name and password not valid plz Enter valid user name and password : ')
        continue
print('Access Granted')
