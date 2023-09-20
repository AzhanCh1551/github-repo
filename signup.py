
database={'Hamza':1212, 'User':1234, 'Admin':0000}
def sin():
    nusername=input(('Enter your username'))
    while nusername in database.keys():
        print("user already exist")
        nusername=input(('Enter different username'))
    npassword=int(input('enter pincode'))
    new={nusername:npassword}
    database.update(new)

def log():
    username=input("Enter username: ")
    password=int(input("Enter pincode"))
    if username in database.keys() and password== database[username]:
        print("Login successful")
        return True    
    else:
        print("Wrong information")
        return False
def Abank():
    current_balance = 2000
    saving_balance = 500
    updated_balance=0

    print("                    Entering bank system...\nFor cheaking your current balance.    Press 1\nFor making a withdraw.    Press 2\nFor deposit amount.    Press 3\nFor transfer amount to your saving account.    Press 4\nFor Exit bank service.    Press 5")
    b=int(input("What do you want to perform"))
    if b==1:
        print("Your current balance is",current_balance)
    elif b==2 :
        withdraw=int(input("Enter amount you want to withdraw"))
        if withdraw>current_balance:
            print("Insufficient Funds")
        else:
            updated_balance = current_balance-withdraw
            current_balance = updated_balance
            print("You withdraw {} from your account".format(withdraw))
            print("Your remaining balance is: ",updated_balance)
    elif b==3:
        deposit=int(input("Enter amount you want to deposit"))
        updated_balance = current_balance+deposit
        current_balance = updated_balance
        print("You deposit {} from your account".format(deposit))
        print("Your remaining balance is: ",updated_balance)
    elif b==4:
        transfer=int(input("Enter amount you want to transfer to your saving account"))
        if transfer>current_balance:
            print("Insufficient Funds")
        else:
            updated_balance = current_balance-transfer
            current_balance = updated_balance
            updated_balance = saving_balance+transfer
            saving_balance = updated_balance
            print("You transfer {} to your saving account".format(transfer))
            print("Your current balance is: ",current_balance)
            print("Your saving balance is: ",saving_balance)
    
    elif b==5:
        print("Thankyou for using our service")
    else:
        print("You have enter an invalid process")

print("Do you want to sign up")
a='1'
z=input("Press 1 for yes \npress 0 for no\n")
if z==a:
    sin()
else:
    print("Now you can login")
print("                Login...")
while True:
    if log():
        a="y"
        while a=="y":
            Abank()
            a=str(input("if you want to continue press y or n for exit"))
            if(a=="n"):    
                print("thanks for using our service")
        break
