# Write a code that the reverses the order of the items means in opposite order.

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# newlist=[]
# for i in range(len(places)):
#     newlist.insert(i,places[-1])
#     places.pop(-1)
# print(newlist)


places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
i = 1
while i<=len(places):
    a = places[-i]
    i+=1
    print(a)