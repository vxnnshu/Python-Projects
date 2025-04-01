# Kaun Banega Crorepati (KBC)

print("Hey, Hello there welcome to the kbc game")

# def questions(a,b,c) : 
#     if (a==True):
#         print("You won $100")
#     else :
#         print("You got this question wrong")

totalmoney=0

print("1st-Q : What is the capital of Australia?")
list1 = ["1-Canberra" , "2-Sydney","3-Melbourne","4-Darwin"]
for item in list1:
    print(item)
# list1[0]=True
# list1[1]=False
# list1[2]=False
answer1=input("Enter Your Answer : ").lower()
if (answer1=="canberra"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You Got This Question Wrong")
# if answer1(answer1=True):
#     print("You Won $100 :)")
# else :
#     print("You Got This Question Wrong :(")

print("2nd-Q : What is the largest planet in our Solar System")
list2 = ["1-Pluto", "2-Mars","3-Jupiter","4-Earth"]
for item in list2:
    print(item)
answer2=input("Enter your answer here : ").lower()
if (answer2=="jupiter"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You got this question wrong")

print("3rd-Q : What is the Chemical Symbol for water")
print("Write this answer with correct spelling**")
list3 = ["1-He", "2-Co2","3-O2","4-H2O"]
for item in list3:
    print(item)
answer3=input("Enter your answer here : ")
if (answer3=="H2O"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You got this question wrong")

print("4th-Q : When Did World War 2 End?")
list4 = ["1-1945", "2-1939","3-1950","4-1944"]
for item in list4:
    print(item)
answer4=input("Enter your answer here : ")
if (answer4=="1945"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You got this question wrong")

print("5th-Q : What is the tallest mountain in the world?")
list5 = ["1-Lhotse", "2-K2","3-Kanchenjunga","4-Everest"]
for item in list5:
    print(item)
answer5=input("Enter your answer here : ").lower()
if (answer5=="everest"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You got this question wrong")

print("6th-Q : What planet is known as the Red Planet?")
list6 = ["1-Venus", "2-Uranus","3-Earth","4-Mars"]
for item in list6:
    print(item)
answer6=input("Enter your answer here : ").lower()
if (answer6=="mars"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You got this question wrong")

print("7th-Q : What is the square root of 4761?")
list7 = ["1-73", "2-48","3-69","4-70"]
for item in list7:
    print(item)
answer7=input("Enter your answer here : ")
if (answer7=="69"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You got this question wrong")

print("8th-Q : What is the hardest natural substance on Earth?")
list8 = ["1-Diamond", "2-Ruby","3-Gold","4-Iron"]
for item in list8:
    print(item)
answer8=input("Enter your answer here : ").lower()
if (answer8=="diamond"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You got this question wrong")

print("9th-Q : What is the largest country in the world by land area?")
list9 = ["1-India", "2-U.S.A","3-Russia","4-Canada"]
for item in list9:
    print(item)
answer9=input("Enter your answer here : ").lower()
if (answer9=="russia"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You got this question wrong")

print("10th-Q : Who invented the telephone?")
list10 = ["1-Thomas Edison", "2-Nikola Tesla","3-Alexander Graham Bell","4-Michael Faraday"]
for item in list10:
    print(item)
answer10=input("Enter your answer here : ").lower()
if (answer10=="Nikola Tesla"):
    totalmoney+=100
    print("You Won $100")
else:
    print("You got this question wrong")
    
print("The Game Ended :)")
print("You Managed To Win :$ ", totalmoney)