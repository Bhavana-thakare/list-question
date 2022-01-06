#  Write a program in python which display only those names from the list which have ‘i’ as second last character.

L = ["Amit" , "Suman" , "Sumit" , "Montu" , "Anil"]
for i in L:
     if i[-2]=='i':
         print(i)
