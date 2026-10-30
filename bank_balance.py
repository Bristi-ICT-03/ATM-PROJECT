balance=1000
while True:
    print("-----ATM MENU-----")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    n=int(input("Enter your choice: "))
    if(n==1):
        print(f"your current value is: {balance} ")
    elif(n==2):
        k=int(input("Enter your deposit amount: "))
        if(k>0):
            print("Deposit Successful")
            balance=balance+k
            print(f"Updated Balance: {balance}")
    elif(n==3):
        l=int(input("Enter your withdrawal amount: "))
        if(l<=balance):
            print("Please collect your cash")
            balance=balance-l
            print(f"current Balance: {balance}")
        else:
            print("Insufficient balance")
            print(f"current Balance: {balance}")
            
    elif(n==4):

        print("Exit Program")

        print("Thank you for using the ATM")

        print("Have a nice day!")
        break



