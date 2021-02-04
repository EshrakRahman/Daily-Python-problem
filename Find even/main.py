user_input = int(input())
max_number = 2
if user_input < 200:
    if user_input % 2 == 0:
        for i in range(max_number, user_input, 2):
            print(i)

    elif user_input % 2 != 0:
        user_input += 1
        for j in range(max_number, user_input, 2):
            print(j)
