#binary to decimal

# binary=[1, 0, 0, 1, 1, 0, 1, 1]
# a = 0 
# for i in binary: 
#     a = a*2 + i
# print("The decimal value is:", a)

# binary=[1, 0, 0, 2, 1]
# a = 0 
# for i in binary: 
#     a = a*2 + i
# print("The decimal value is:", a)

binary = 100011
a = 0
decimal = 0
while (binary != 0):
    b= binary % 10
    binary = binary // 10
    b = b*pow(2, a)
    decimal= decimal + b
    a = a+1
print(decimal)
