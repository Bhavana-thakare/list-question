givenlist=[1,3,4,7,11,13]
newlist=list(range(givenlist[0],givenlist[-1]+1))
missingnumber=set(givenlist)^set(newlist)
print("missing number in given list=",missingnumber)