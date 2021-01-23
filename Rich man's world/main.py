amount = int(input())
total_amount = 700000
year = 0
while amount <= total_amount:
    if 50000 < amount <= total_amount:
        amount = amount * float(1.071)
    year += 1

print(year)
