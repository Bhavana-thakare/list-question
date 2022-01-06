# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# sum = 0
# j=0
# for i in marks:
#     for j in i:
#         sum = sum + j
# print(sum)

# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
# sum = 0
# j=0
# for i in marks:
#     for j in i:
#         sum = sum + j
# print(sum)

# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
# sum=0
# j=0
# for i in marks:
#     for j in i:
#         sum = sum + j
# print(sum)

marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks = 0
counter = 0
while counter < len(marks):
    total_marks = total_marks + int(marks[counter])
    counter = counter + 1
print(total_marks)