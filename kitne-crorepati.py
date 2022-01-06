i=0
a=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
co=0
count=0
counter=0
while i<len(a):
    if a[i]>10000000 and a[i]<1000000000:
        count=count+1
    elif a[i]>100000 and a[i]<10000000:
        co=co+1
    else:
        counter=counter+1
    i+=1
print(counter,"crorepati hai")
print(co,"Lakhpati hai")
print(counter,"Dilwale hai")