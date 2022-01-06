#counts the numbers more then 20 and 40 and then print its count.

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
lessthen20=0
morethen40=0
i=0
while i<len(numbers):
    b=numbers[i]
    if b<20:
        lessthen20=lessthen20+1
    else:
        morethen40=morethen40+1
    i+=1
print("lessthen20:"+str(lessthen20))
print("morethen40:"+str(morethen40))            


