# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

months = 0

while principal > 0:
    months += 1
    if (principal * (1+rate/12) - payment) < 0:
        payment = principal * (1+rate/12)

    principal = principal * (1+rate/12) - payment
    total_paid += payment
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    #print(months, round(total_paid, 2), round(principal, 2))
    print(f'{months:>3} {total_paid:0.2f} {principal:0.2f}')


# print('Total paid', round(total_paid,2))
# print('Months', months)

print(f'Total paid {total_paid:0.2f}\nMonths {months}')

# Excercise 1.12: A mystery
#   bool('False') evaluates to true because the string literal is not none