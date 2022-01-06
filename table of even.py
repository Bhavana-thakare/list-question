# Write a program in python which print the table of first even number.

L = [23, 13, 101, 6, 81, 9, 4]
for i in range(len(L)):
     if L[i]%2==0:
         for j in range(1,11):
              print(L[i] * j)
         break
L[i]=L[i]+1


