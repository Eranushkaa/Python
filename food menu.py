print("Name: Anushka Porwal ")
print("Roll No: 0863CS241039")

def show(menu):
    print('*' * 30)
    print('Welcome to the Cherry Hotel')
    print('*' * 30)

    for a, b in menu.items():
        print(f'{a} ---> Rs. {b}')

    print('*' * 30)


def order(menu):
    total = 0
    order_list = {}

    while True:
        item = input('Enter the item you want to order (e to exit): ').strip().title()

        if item == 'E':
            break

        if item not in menu:
            print('Item not found in the menu.')
            continue

        try:
            qty = int(input(f'Enter the quantity of {item}: '))
            if qty <= 0:
                print('Quantity must be greater than zero.')
                continue
        except ValueError:
            print('Please enter a valid quantity.')
            continue

        amount = menu[item] * qty

        if item not in order_list:
            order_list[item] = {'qty': qty, 'amount': amount}
        else:
            order_list[item]['qty'] += qty
            order_list[item]['amount'] += amount

        total += amount
        print('Added to order list.')

    print('*' * 30)
    print('BILL:')
    print('*' * 30)

    for item, details in order_list.items():
        print(f"{item} x {details['qty']} = Rs. {details['amount']}")

    print('*' * 30)
    print(f'Total Amount: Rs. {total}')
    print('*' * 30)
    print('Visit again!')
    print('*' * 30)


def main_menu():
    menu = {
        'Samosa': 20,
        'Kachori': 20,
        'Poha': 15,
        'Jalebi': 40,
        'Tea': 10,
        'Coffee': 25,
        'Vada': 30
    }

    show(menu)
    order(menu)


main_menu()
