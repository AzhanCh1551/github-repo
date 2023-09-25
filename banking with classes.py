database={'azhan':1551, 'sohaib':7232, 'sameer':1192}
def sign_up():
    nusername = input("Enter your username: ")
    while nusername in database.keys():
        print("User already Exist")
        input("Enter another Username: ")
    npassword=int(input("Enter your pin code: "))
    new={nusername:npassword}
    database.update(new)

def login():
    username=input("Enter your username: ")
    password=int(input("Enter your pin code: "))
    
    if username in database.keys() and password in database.values():
        print("Login Successful")
        return True
    else:
        print("Wrong information")
        return False
             
class Banking:
    def __init__(self):
        self.balance=50000
        print("wellcome to MBL bank")
    def show_amount(self):
        print("your current balance is ",self.balance)
    def withdraw(self,amount):
        
        if amount > self.balance:
            print("Insuficent Funds")
        else:
            updated_balance=self.balance-amount
            print(f"You withdraw {amount} from your acount\nYour new balance is {updated_balance}")
    def Deposit(self,amount):
        updated_balance=self.balance+amount
        print(f"You deposit {amount} in your account\nYour new balance is {updated_balance}")
    
def system():
    print("                    Entering bank system...\nFor cheaking your current balance.    Press 1\nFor making a withdraw.    Press 2\nFor deposit amount.    Press 3\nFor Exit bank service.    Press 4")
    b=int(input("What do you want to perform: "))
    # c = Banking()
    if b==1:
        c = Banking()
        c.show_amount()
    elif b==2:
        w=Banking()
        amount=int(input("Enter amount you want to withdraw: "))
        w.withdraw(amount)
    elif b==3:
        d = Banking()
        amount=int(input("Enter amount you want to deposit: "))
        d.Deposit(amount)
    elif b==4:
        print("Thank you for using our service")
    else:
        print("Invalid process")

print("Dou you want to sign up")
z=int(input("Press 1 for Yes\nPress 0 for No\n-> "))
if z==1:
    sign_up()
elif z==0:
    print("You can now Login")

else:
    print("Invalid Choice")
print("              Login...")
while True:
    if login():
        a="y"
        while a=="y":
            system()
            a=input("If you want to do another process press y\nIf you want to quit press n\n-> ")
            if (a=="n"):
                print("Thanks for using our service")
        break