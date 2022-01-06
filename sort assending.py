list=[15,4,56,8,1,35,2,9]
i=0
while i<len(list):
    j=0
    while j<i:
        if list[i]<list[j]:
            b=list[i]
            list[i]=list[j]
            list[j]=b
        j+=1
    i+=1
print(list)





# lst=[9,8,7,6,5,4,3,2,1,0]
# for j in range(0,9):
#     for i in range(0,9):
#         if lst[i]>lst[i+1]:
#             swap=lst[i]
#             lst[i]=lst[i+1]
#             lst[i+1]=swap
# print(lst)