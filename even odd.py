list1=[8,4,9,17,13,14]
i=0
even=[]
odd=[]
while i<len(list1):
    j=list1[i]
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
    i=i+1
print("even number",even)
print("odd number",odd)