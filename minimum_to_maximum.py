data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []
while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    
print (new_list)






# data = [3, 1, 5, 2, 4]
# n = len(data)
# for i in range(n):
#     for j in range(1,n):
#         if data[j-1] > data[j]:
#             (data[j-1], data[j]) = (data[j], data[j-1])
# print(data)



