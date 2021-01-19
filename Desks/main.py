# reads number of student in the class
group_one_student = int(input())
group_two_student = int(input())
group_three_student = int(input())

# calculate required desk
group_one_desk = group_one_student // 2
group_two_desk = group_two_student // 2
group_three_desk = group_three_student // 2

# if the number is odd
odd_group_one = group_one_student % 2
odd_group_two = group_two_student % 2
odd_group_three = group_three_student % 2

# total desk required
total_desk = group_one_desk + group_two_desk + group_three_desk + odd_group_one + odd_group_two + odd_group_three
print(total_desk)
