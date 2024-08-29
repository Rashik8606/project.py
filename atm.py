class banking():
    def __init__(self,name,acc_no):
        self.name = name
        self.acc_no = acc_no
        self.balance = 0

    def display(self):
        print("______Account Details______")
        print(f"Your name : {self.name}")
        print(f"Acc/no :  {self.acc_no}")
        print()
        print(f"1.deposit\n2.withdraw\n3.balance\n4.exit")

    def deposit(self,amount):
        self.balance+=amount
        print(f"Amount Added  {amount}")
        print(f"your balance {self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-= amount
            print(f"Your Withdraw an Amount of Rs : {amount}")
        else:
            print("Insufficient funds!")
        print(f"your Balance : {self.balance}")

    def balance1(self):
        return self.balance

    def exit(self):
        print('exiting...')


acc_name = input('Enter your name :')
acc_no = input('Enter Your Account Number :')
obj = banking(acc_name,acc_no)
while True:
    obj.display()

    choice = int(input('Select Your option '))
    if choice==1:
        deposit = int(input("Enter the Amount you want to add :"))
        obj.deposit(deposit)
    elif choice==2:
        withdraw = int(input('Enter the Amount :'))
        obj.withdraw(withdraw)
    elif choice==3:
        print(f"your balance {obj.balance1()}")
    elif choice==4:
        obj.exit()
        break
    else:
        print('invalid')


