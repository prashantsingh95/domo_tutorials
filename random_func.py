import random

def magix(num):
    if num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return '4'
    elif num == 5:
        return '5'
    elif num == 6:
        return '6'
r = random.randint(1,6)
ge = magix(r)
print(ge)