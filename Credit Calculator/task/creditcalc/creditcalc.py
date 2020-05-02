import argparse as argp
import math
import sys

def monthly_interest_rate(interest):
    return interest / (12 * 100)


def months_count(payment, month_rate, principle):
    x = payment / (payment - (month_rate * principle))
    base = 1 + month_rate
    return math.ceil(math.log(x, base))


def calc_equation_second_half(month_rate, months):
    return (month_rate * math.pow((1 + month_rate), months)) / (math.pow((1 + month_rate), months) - 1)


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
    mp = math.ceil(cp * calc_equation_second_half(monthly_interest_rate(ci), cm))
    print(f'Your annuity payment = {mp}!')


def credit_principal():
    # Annuity Monthly Payment
    amp = float(input('Enter monthly payment:\n'))
    # Count of Months
    cm = int(input('Enter count of periods:\n'))
    # Credit Interest
    ci = float(input('Enter credit interest:\n'))
    cp = round(amp * (1 / calc_equation_second_half(monthly_interest_rate(ci), cm)))
    print(f'Your credit principal = {cp}!')


parser = argp.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()
received_args_num = len(sys.argv) - 1

process_type = args.type
mp = args.payment
cp = args.principal
periods = args.periods
ci = args.interest
print(received_args_num)




