'''
This Program Will Tell You The Area And Circumference Of The Given Values      2pir c    pir2 a
'''
print("What Would You Like To Calculate")
print("1-Area Of The Circle")
print("2-Circumference/Perimeter Of The Circle")
choice = input("Enter 1 For Area or Enter 2 For Circumference : ")

#Checking If Choice Is Valid Or Not
if choice not in ['1','2']:
    print("Choice Is Invalid")
else : 
    radius = float(input("Enter The Radius Of Circle : "))

#Perform The Calculation
if choice == '1':
    area = 3.14 * radius * radius
    print(f"The Area Of This {radius} is {area}")
elif choice == '2':
    circumference = 2 * 3.14 * radius
    print(f"The Circumference/Perimeter Of This {radius} is {circumference}")