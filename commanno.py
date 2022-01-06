# list1= [1,2,3,4,5,6]
# list2= [2,3,1,0,6,7]
# z=[]
# for i in list1:
#     if i in list2:
#         z.append(i)
# print("the common element are",z)

list1 = [1,2,3,4,5,6]  
list2 = [7,8,9,2,10]  
for x in list1:  
    for y in list2:  
        if x == y:  
            print("The common element is:",x)  