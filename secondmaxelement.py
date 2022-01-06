# second maximum number

number= [50, 40, 23, 70, 56, 12, 5, 10, 7]
a=max(number[0],number[1])
secondmax=min(number[0],number[1])
n =len(number)
for i in range(2,n):
    if number[i]>a:
        secondmax=a
        a=number[i]
    elif number[i]>secondmax:
        a != number[i]
        secondmax=number[i]
print(secondmax)