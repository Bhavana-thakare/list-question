list=[38,5,10,35,39,86,85,87,20]
i=0
l=[]
while i<len(list):
    if list[i]%5==0:
        l.append(list[i])
    i=i+1
print(l)