List1 = [ ]
List2 = [ ]
for i in range(10):
     k = int(input("Enter any number : "))
     if k%2==0:
        List1.append(k)
     else:
        List2.append(k)
print("Even number List :",List1)
print("Odd number List :",List2)