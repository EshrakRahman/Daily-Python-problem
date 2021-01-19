# Reads hours input one by one

recommended_sleep_hours = int(input())  # A hours
sleep_not_more_than = int(input())  # B hours
anna_sleep = int(input())  # H hours

if anna_sleep < recommended_sleep_hours:
    print('Deficiency')
elif anna_sleep > sleep_not_more_than:
    print('Excess')
else:
    print('Normal')
