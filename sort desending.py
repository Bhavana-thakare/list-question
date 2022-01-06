list=[15,4,56,8,1,35,2,9]
i=0
while i<len(list):
    j=0
    while j<i:
        if list[i]>list[j]:
            b=list[i]
            list[i]=list[j]
            list[j]=b
        j+=1
    i+=1
print(list)


