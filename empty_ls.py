name_ls = []
c = 0
while True:
    c = c + 1
    print('Enter name', c)

    name = input()
    if name == '':
        break
    name_ls = name_ls + [name]
print('name ')
for name in name_ls:
    print('  '+ name)

