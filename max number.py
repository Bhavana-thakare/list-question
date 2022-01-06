n=[50,4,23,70,56,12,5,10,7]
i=0
max=n[0]
while i<len(n):
    num=n[i]
    if num>max:
        max=num
    i=i+1
print(max)