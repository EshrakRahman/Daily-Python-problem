# Reads two input as row and column
column = int(input())
row = int(input())

if column == 1 and row == 1 or column == 1 and row == 8:
    print('3')
elif column == 8 and row == 1 or column == 8 and row == 8:
    print('3')
elif column == 1 and 8 > row > 1 or column == 8 and 8 > row > 1:
    print('5')
elif 9 > column > 0 and row == 1 or 9 > column > 0 and row == 8:
    print('5')
else:
    print('8')
