#sum of number in list

a=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the number:"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print("sum of list is ",sum)

