a=[3,5,6,7,8]
b=[10,2,4,2,6]
i=0
sum=0
c=[]
while i<len(a):
    sum=sum+a[i]+b[i]
    c.append(a[i]+b[i])
    i+=1
print(c)
print(sum)