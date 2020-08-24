# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0
    for row in rows:
        try:
            total_cost += int(row[1]) * float(row[2])
        except ValueError:
            print('Value error, missing data')

    f.close()

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'missing.csv'

cost = portfolio_cost('Data/' + filename)
print('Total Cost:', cost)