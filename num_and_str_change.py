l=[10,"FUN",40,"FEW",50,"FULL"]
for i in range (len(l)):
    if type(l[i])==int:
        l[i]=l[i]**2
    elif type(l[i]==str):
        l[i]=(l[i]).swapcase()
print(l)