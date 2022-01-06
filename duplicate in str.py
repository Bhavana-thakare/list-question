string="python programming"
duplicates=[]
for i in string:
    if string.count(i)>1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)


