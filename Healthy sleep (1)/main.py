# Takes three input as a hours
required_sleep = int(input())
over_sleep = int(input())
ann_sleeps = int(input())

if required_sleep <= over_sleep:
    if over_sleep >= ann_sleeps >= required_sleep:
        print('Normal')

    elif ann_sleeps <= required_sleep:
        print('Deficiency')

    elif ann_sleeps >= over_sleep:
        print('Excess')
