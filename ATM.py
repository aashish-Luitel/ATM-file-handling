print("====================")
print("WELCOME    TO    ATM")
print("====================")
name = "Aashish luitel"
pin = "****"
with open("balance.txt", "r") as file:
    balance = int(file.read())
password = input("Please enter your PIN : ")
while pin != password:
    print("OOPS! YOUR PIN SEEMS TO BE INVALID.....")
    print("PLEASE RE-ENTER YOUR PIN:")
    password = input()
print("1. USER DETAILS")
print("2. CHECK BALANCE")
print("3. WITHDRAW MONEY")
print("4. DEPOSIT MONEY")
print("5. EXIT")

choice = int(input("PLEASE ENTER YOUR CHOICE :"))

if choice == 1:
    print("NAME = MICHAEL JACKSON")
    print("BALANCE = ", balance)

    print("HAVE A GREAT DAY")
    
elif choice == 2:
    print("YOUR BALANCE IS = ", balance)

    print("HAVE A GREAT DAY")
    
elif choice == 3:
    withdraw = int(input("ENTER AMOUNT FOR WITHDRAWL :"))
    if withdraw <= 0:
        print ("INVALID AMOUNT!")
    elif withdraw >= 0:
        balance = balance - withdraw
        with open("balance.txt", "w") as file:
            file.write(str(balance))
        print ("WITHDRAWAL SUCCESSFUL!")
        print ("Remaining balance :", balance)

        print("HAVE A GREAT DAY")
        
elif choice == 4:
    deposit = int(input("ENTER AMOUNT FOR DEPOSITION :"))
    if deposit <= 0:
        print("INVALID AMOUNT")
    elif deposit >= 0:
        balance = balance + deposit
        with open("balance.txt", "w")as file:
            file.write(str(balance))
        print("DEPOSITION SUCCESSFUL!")
        print("NEW BALANCE :", balance)

        print("HAVE A GREAT DAY")

elif choice == 5:
    print("HAVE A GREAT DAY")



