a = ['cat', 'dog', 'cat', 'mouse', 'dog']
i = 0
while i < len(a):
    j = i + 1
    while j < len(a):
        if a[i] == a[j]:
            del a[j]
        else :
            j += 1
    i += 1
print(a)