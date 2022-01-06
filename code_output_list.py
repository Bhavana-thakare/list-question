# geekCodes = [1, 2, 3, 4]
# geekCodes.append([5,6,7,8])
# print(geekCodes)


# check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
# check2 = check1
# check3 = check1[:]
# check2[0] = 'Code'
# check3[1] = 'Mcq'
# count = 0
# for c in (check1, check2, check3):
#     if c[0] == 'Code':
#         count += 1
#     if c[1] == 'Mcq':
#         count += 10
# print (count)



# list1 = range(100, 110)
# print (list1.index(105))


 
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list2[0] = 0; 
# print( list1) 


# List1 = [1998, 2002]
# List2 = [2014, 2016]
# print ((List1 + List2)*2)

# list = [1, 2, 3, None, (1, 2, 3, 4, 5), ['Geeks', 'for', 'Geeks']]
# print(len(list))
# print(list)


# print(list( range(4, 30, 2)))


# for i in range(4,31):
#     if i%2 == 0:
#         print(i, end=' ')
 

# a=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# for i in a:
#     if i%2==0:
#         print(i, end=' ')


# Index=int(input("num"))
# n=0
# for x in range (0,Index+1):
#    n+=x
# print(n)


# list1 = [4, 6, 8, 24, 12,2]
# max= sorted(list1)
# print(max[-1])


# list = []
# list_1 =[]
# n = int(input("enter the total numbers inside list.:"))
# i = 1
# while(i <= n):
#    num = int(input("enter the numbers you want to insert into list:"))
#    i +=1
#    list.append(num)
# print(list, " <--the given list by you is here.\n ")
# list.sort()
# print(list)
# print(max(list))


# list=[]
# def l(a,b):
#     for i in range(a,b):
#         if i%2==0:
#             c=list.append(i)
#     return c
# v=l(4,30)
# print(v)


# numList = []
# def PythonList(start, end):
#     for x in range(start, end):
#         if x % 2 == 0:
#             numList.append(x)
#     return numList
# print (PythonList(4, 30))

 
# def cal(n):
#     sum=0
#     for i in range(1, n, 1):
#         sum = sum +i
#     print(sum)
# rev = cal(11)

# aList = [4, 6, 8, 24, 12, 2]
# aList.sort(reverse=True)
# print(aList.pop(0))


# def findDigitsCharsSymbols(inputString):
#    charCount = 0
#    digitCount = 0
#    symbolCount = 0
#    for char in inputString:
#         if char.islower() or char.isupper():
#            charCount+=1
#         elif char.isnumeric():
#            digitCount+=1
#         else:
#             symbolCount+=1
#    print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
# inputString = "P@#yn26at^&i5ve"
# print("total counts of chars, digits,and symbols ")
# findDigitsCharsSymbols(inputString)


# def shift_first_last(lst):
#     x = lst.pop(0)
#     y = lst.pop()
#     lst.insert(0, y)
#     lst.insert(len(lst), x)
#     return lst

# nums = [1,2,3,4,5,6,7]
# print("Original list:")
# print(nums)
# print("Shift last element to first position and first element to last position of the said list:")
# print(shift_first_last(nums))



