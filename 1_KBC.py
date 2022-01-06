# question_list=[
#     "Who is the Father of our Nation?🤔",
#     "Who was the first Prime Minister of India?🤔",
#     "Who wrote Romeo and Juliet?🤔",
#     "Which organ purify our blood?🤔",
#     "When do we celebrate our Independence Day?🤔"
# ]
# option_list=[
#     ["Dr. B. R. Ambedkar","Jawaharlal Nehru","Mahatma Gandhi","Bhagat Singh"],
#     ["Tantia Tope","Jawaharlal Nehru","Vinayak Damodar Savarkar","Mahatma Gandhi"],
#     ["William Shakespeare","William Faulkner","Raja Rao","James Patterson"],
#     ["heart","lungs","intersitne","kidney"],
#     ["22 aug","15 aug","26 jan","2 oct"],
# ]
# op50_50=[
#     ["2.Jawaharlal Nehru","3.Mahatma Gandhi"],
#     ["1.Tantia Tope","2.Jawahrlal Nehru"],
#     ["1.William Shakespeare","4.James patterson"],
#     ["1.heart","4.kidney"],
#     ["1.22 aug","2.15 aug"]
# ]
# answer_list=[3,2,1,4,2]
# print("💸--💰kon banega karodpati💰--💸")
# print("lets start the game>>\n")
# i=0
# c=0
# s=10000
# while i<len(question_list):
#     print(question_list[i])
#     a=0
#     while a<len(option_list[i]):
#         k=option_list[i][a]
#         print(a+1,k)
#         a=a+1
#     if c==0:
#         life_line=input("Do you want to take lifeline?🧐..")
#         if life_line=="yes":
#             c+=1
#             print(op50_50[i])
#             s+=10000
#     Ans=int(input("Enter the option🙂:"))
#     if answer_list[i]==Ans:
#         print("your answer is correct😍,you won",s,"rupees🤑\n")
#         s+=10000
    
#     else:
#         print("🥺Your answer is wrong🥺\n")
#         print("\t\t~~😵Game over😵~~")
#         break
#     i+=1









question_list = [
"How many continents are there?🤔", # pehla question
"What is the capital of India?🤔", # doosra question
"NG mei kaun se course padhaya jaata hai?🤔" # teesra question
]
option_list = [
#pehle question ke liye options
["Four", "Nine", "Seven", "Eight"],
#second question ke liye options
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#third question ke liye options
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
op50_50=[
    ["2.Nine","3.Seven"],
    ["3.Bhopal","4.Delhi"],
    ["1.Software Engineering","4.Agriculture"]
]
# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
print("💸--💰kon banega karodpati💰--💸")
print("lets start the game>>\n")
i=0
c=0
s=10000
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<len(option_list[i]):
        k=option_list[i][a]
        print(a+1,k)
        a=a+1
    if c==0:
        life_line=input("Do you want to take lifeline?🧐..")
        if life_line=="yes":
            c+=1
            print(op50_50[i])
            s+=10000
    Ans=int(input("Enter the option🙂:"))
    if solution_list[i]==Ans:
        print("your answer is correct😍,you won",s,"rupees🤑\n")
        s+=10000
    
    else:
        print("🥺Your answer is wrong🥺\n")
        print("\t\t~~😵Game over😵~~")
        break
    i+=1


