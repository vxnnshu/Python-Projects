print("Welcome To Python Bank")

account_number = input("Enter Your Account Number : ")
if len(account_number) != 10 :
    print("Account Is Incorrect, Try Again")
    exit()
account_number = int(account_number)

pin = input("Enter Your 4 Digit Pin : ")
if len(pin) != 4 : 
    print("Pin Is Wrong")
    exit()
pin = int(pin)

print("What Would You Like To Do")
print("1: Withdraw")
print("2: Deposit")
print("3: Check Balance")
print("4: Exit")

money = 10000
check_balance = money

choice = int(input("Enter Your Choice : "))

if (choice > 4) : 
    print("Invalid Choice")
else :
    pass

if (choice == 1 ) : 
    withdraw = int(input("Enter The Amount Of Withdrawl : " ))
    print(f"The Amount {withdraw} Has Been Successfully Withdrawled")
    check_balance = money - withdraw
    print(f"Your Balance Is : {check_balance}")

elif (choice == 2) : 
    deposit = int(input("Enter The Amount That You Want To Deposit : "))
    print(f"The Amount {deposit} Has Been Deposited In Your Account")
    check_balance = money + deposit
    print(f"Your Balance Is : {check_balance}")
    
elif (choice == 3) : 
    print(f"Your Balance Is : {check_balance}")

elif (choice == 4) : 
    print("You Can Exit")

else : 
    print("Invalid Choice!")