parts = {'PC': 10, 'Laptop': 30, 'Keyboard': 5}

def show():
    print('Current inventory')
    for k, v in parts.items():
        print(k, ':', v)


def update_inventory(name, number):
    if parts[name] >= number:
        parts[name] -= number
    else:
        print("We do not have enough")


def ask_user():
    item_name = input('Which item you want to buy or X to exit: ')
    if item_name in parts:
        number = int(input('How many item you want to buy: '))
        update_inventory(item_name, number)
    elif item_name != 'X':
        print('Item not exist')
    else:
        return  'X'

ans = ''
while ans != 'X':
    show()
    ask_user()