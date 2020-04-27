from math import ceil

principal = float(input('Enter the credit principal:\n'))
print('What do you want to calculate?')
print('type "m" - for count of months,')
print('type "p" - for monthly payment:')
chosen = input()

if chosen == 'm':
    payment = float(input('Enter monthly payment:\n'))
    months = ceil((principal / payment))
    print(f'\nIt takes {months} months to repay the credit')
elif chosen == 'p':
    months = float(input('Enter count of months:\n'))
    payment = ceil((principal / months))
    last_payment = ceil(principal - (months - 1) * payment)
    if payment == last_payment:
        print(f'\nYour monthly payment = {payment}')
    else:
        print(f'\nYour monthly payment = {payment} with last month payment = {last_payment}.')
