# Reads three input
first_number = float(input())
second_number = float(input())
operation = str(input())

if operation == '+':
    print(first_number + second_number)

elif operation == '-':
    print(first_number - second_number)

elif operation == '/' and second_number == 0:
    print('Division by 0!')

elif operation == '/':
    print(first_number / second_number)

elif operation == '*':
    print(first_number * second_number)

elif operation == 'mod' and second_number == 0:
    print('Division by 0!')

elif operation == 'mod':
    print(first_number % second_number)

elif operation == 'pow':
    print(first_number ** second_number)

elif operation == 'div' and second_number == 0:
    print('Division by 0!')

elif operation == 'div':
    print(first_number // second_number)
