# Reads two input as number and highest number
student_score = float(input())
maximum_score = float(input())

# Calculate grade by its maximum number
a_grade = (student_score * 100) / maximum_score
b_grade = (student_score * 100) / maximum_score
c_grade = (student_score * 100) / maximum_score
d_grade = (student_score * 100) / maximum_score


if 90 <= a_grade <= 100:
    print('A')

elif 80 <= b_grade < 90:
    print('B')

elif 70 <= c_grade < 80:
    print('C')

elif 60 <= d_grade < 70:
    print('D')

else:
    print('F')
