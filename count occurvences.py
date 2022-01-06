# list=["a","R","a","d","a","f","b","a","d","R"]
# i=0
# m=[]
# while i<len(list):
#     b=0
#     count=0
#     n=[]
#     while b<len(list):
#         if list[i]==list[b]:
#             count=count+1
#         b=b+1
#     n.append(list[i])
#     n.append(count)
#     if n not in m:
#         m.append(n)
#     i=i+1
# print(m)

list=input("Enter the character:")
i=0
m=[]
while i<len(list):
    b=0
    count=0
    n=[]
    while b<len(list):
        if list[i]==list[b]:
            count=count+1
        b=b+1
    n.append(list[i])
    n.append(count)
    if n not in m:
        m.append(n)
    i=i+1
print(m)
