# This program is made to that you dont have to calculate the percentage of your
# exam marks this program will get your percentage.. you just have to put your marks here.

SST=float(input("Enter Your SST Marks : "))
ENGLISH=float(input("Enter Your ENGLISH Marks : "))
MATHS=float(input("Enter Your MATHS Marks : "))
SCIENCE=float(input("Enter Your SCIENCE Marks : "))
HINDI=float(input("Enter Your HINDI Marks : "))

totalmarks = 400
marksobtained= SST+ENGLISH+MATHS+SCIENCE+HINDI
# print(marksobtained)

percentage=marksobtained/totalmarks*100
print(percentage)