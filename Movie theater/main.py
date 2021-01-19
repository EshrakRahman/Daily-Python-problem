# Read all the input from user
number_of_halls = int(input())
capacity = int(input())
number_of_viewers = int(input())

print(number_of_halls > 0 and (number_of_halls * capacity) >= number_of_viewers)
