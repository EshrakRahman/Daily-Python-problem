# Reading a integer number
first_input = int(input())

for _ in range(first_input):
    others_input = int((input()))
    if others_input % 7 == 0:
        output = others_input * others_input
        print(output)
