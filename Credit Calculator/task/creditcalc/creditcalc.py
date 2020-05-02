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


def months_number(cp, mp, ci):
    i = monthly_interest_rate(ci)
    n = months_count(mp, i, cp)
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


def monthly_payment(cp, periods, ci):
    mp = math.ceil(cp * calc_equation_second_half(monthly_interest_rate(ci), periods))
    print(f'Your annuity payment = {mp}!')
    print(f'Overpayment = {math.ceil((mp * periods) - cp)}')


def credit_principal(mp, periods, ci):
    cp = round(mp * (1 / calc_equation_second_half(monthly_interest_rate(ci), periods)))
    print(f'Your credit principal = {cp}!')
    print(f'Overpayment = {math.ceil((mp * periods) - cp)}')


def diff_payment(cp, periods, ci):
    i = monthly_interest_rate(ci)
    m = 1
    all_payment = 0.0
    while m <= periods:
        val = (cp / periods) + (i * (cp - (cp * (m - 1) / periods)))
        all_payment += val
        print(f'Month {m}: paid out {math.ceil(val)}')
        m += 1
    print(f'Overpayment = {math.ceil(all_payment - cp)}')


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

if received_args_num < 4 or \
        process_type is None or \
        ((process_type != 'annuity' and process_type == 'diff') and
         (process_type == 'annuity' and process_type != 'diff')) or \
        (process_type == 'diff' and mp is not None) or \
        ((mp is not None and mp < 0) or
         (cp is not None and cp < 0) or
         (periods is not None and periods < 0) or
         (ci is not None and ci < 0)) or \
        ci is None:
    print('Incorrect parameters')
elif process_type == 'diff':
    diff_payment(cp, periods, ci)
elif process_type == 'annuity' and mp is None:
    monthly_payment(cp, periods, ci)
elif process_type == 'annuity' and cp is None:
    credit_principal(mp, periods, ci)
elif process_type == 'annuity' and periods is None:
    months_number(cp, mp, ci)


