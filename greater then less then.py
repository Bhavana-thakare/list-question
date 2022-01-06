num=[50,60,23,70,5,4,45,3]
i=0
a=[]
b=[]
while i<len(num):
    j=num[i]
    if j>20:
        a.append(j)
    elif j<40:
        b.append(j)
    else:
        print("invalid")
    i=i+1
print("greater than 20=",a)
print("smaller than 20=",b)