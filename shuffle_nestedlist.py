list= [[1,2,3],[4,5,6],[7,8,9]]
a = []
for i in range(3):
    b = []
    for row in list:
            b.append(row[i])
    a.append(b)
print(a)