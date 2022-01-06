list1=[1,-2,-4,6,7,-23,45,-10]
positive=0
negative=0
for num in list1:
   if num >= 0:
      positive += 1
   else:
      negative += 1
print("Positive numbers in the list is", positive)
print("Negative numbers in the list is", negative)


