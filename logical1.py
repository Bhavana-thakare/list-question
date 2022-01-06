a=["v","y"]
user=int(input("Enter the number:"))
i=1
while i<=user:
    j=0
    while j<len(a):
        print(a[j],i,end="")
        j=j+1
    i=i+1