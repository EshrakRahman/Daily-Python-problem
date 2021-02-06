user_input = []

while True:
    number = input()
    if number == '.':
        break
    else:
        user_input.append(float(number))

print(min(user_input))
