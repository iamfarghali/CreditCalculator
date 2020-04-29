import math


def monthly_interest_rate(interest):
    return interest / (12 * 100)


def months_count(month_payment, month_interest_rate, credit_principle):
    x = month_payment / (month_payment - (month_interest_rate * credit_principle))
    base = 1 + month_interest_rate
    return math.ceil(math.log(x, base))


def months_number():
    # Credit Principle
    cp = float(input('Enter credit principal:\n'))
    # Annuity Monthly Payment
    amp = float(input('Enter monthly payment:\n'))
    # Credit Interest
    ci = float(input('Enter credit interest:\n'))
    i = monthly_interest_rate(ci)
    n = months_count(amp, i, cp)
    years = n // 12
    months = n % 12
    year_flag = 'years' if years > 1 else 'year'
    month_flag = 'months' if months > 1 else 'month'
    if not years == 0 and not months == 0:
        print(f'You need {years} {year_flag} and {months} {month_flag} to repay this credit!')
    elif not years == 0 and months == 0:
        print(f'You need {years} {year_flag} to repay this credit!')
    elif years == 0 and not months == 0:
        print(f'You need {months} {month_flag} to repay this credit!')


def monthly_payment():
    # Credit Principle
    cp = float(input('Enter credit principal:\n'))
    # Count of Months
    cm = int(input('Enter count of periods:\n'))
    # Credit Interest
    ci = float(input('Enter credit interest:\n'))


def credit_principal():
    # Annuity Monthly Payment
    amp = float(input('Enter monthly payment:\n'))
    # Count of Months
    cm = int(input('Enter count of periods:\n'))
    # Credit Interest
    ci = float(input('Enter credit interest:\n'))


print('What do you want to calculate? ')
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment,')
print('type "p" - for credit principal:')
chosen = input()
if chosen == 'n':
    months_number()
elif chosen == 'a':
    monthly_payment()
elif chosen == 'p':
    credit_principal()
