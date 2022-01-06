num=[2,3,7,4,5,6,10,11,120]
largest_num=num[0]
second_largest_num=num[0]
third_largest_num=num[0]
for i in num:
    if i>largest_num:
        third_largest_num=second_largest_num
        second_largest_num=largest_num
        largest_num=i
    elif i>second_largest_num:
        third_largest_num=second_largest_num
        second_largest_num=i
    elif i>third_largest_num:
        third_largest_num=i
print("Third largest number of the list is :",third_largest_num)


