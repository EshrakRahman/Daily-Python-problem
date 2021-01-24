# put your python code here
n = 1

while n > 0:
    user_input = int(input())
    if user_input < 10:
        pass
    if 10 <= user_input <= 100:
        print(user_input)
    if user_input > 100:
        break
