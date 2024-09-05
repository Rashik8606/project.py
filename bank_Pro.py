class Bank_Detils():
    def __init__(self,user_name,user_Accno,balance_user) -> None:
        self.name = user_name
        self.user_accono = user_Accno
        self.balance_user = balance_user

class DepositAccount(Bank_Detils):
    def __init__(self,user_name,user_Accno,balance_user,amount) -> None:
        super().__init__(user_name,user_Accno,balance_user)
        self.amount = amount

    def Deposit1(self):
        self.balance_user+=self.amount
        return self.balance_user

class WithdrawAccount(Bank_Detils):
    def __init__(self, user_name, user_Accno, balance_user,Withdraw_Amot1) -> None:
        super().__init__(user_name, user_Accno, balance_user)
        self.Withdraw_Amout1 = Withdraw_Amot1

    def Withdraw1(self):
        if self.Withdraw_Amout1 <= self.balance_user:
            self.balance_user-=self.Withdraw_Amout1
        else:
            print("Insufficient balance!")
        return self.balance_user

class DisplayAccount(Bank_Detils):
    def __init__(self, user_name, user_Accno, balance_user) -> None:
        super().__init__(user_name, user_Accno, balance_user)
    def Display1(self):
        print(f"Name : {self.name}\n"
              f"Account Number : {self.user_accono}\n"
              f"Balance : {self.balance_user}")
        
def main():
    print("First Your Enter Your Account Details")
    user_name= input("📝Enter Your Name :")
    user_Accno= int(input("🔐Enter your Acct/no :"))
    balance_user = int(input("💸Enter Amount :"))
    
    account = Bank_Detils(user_name,user_Accno,balance_user)
    while True:
        print("1.💵Deposit\n"
            "2.💳Withdraw\n"
            "3.📍Display\n"
            f"4.❌Exit")
        
        choose = int(input("Select Your Option :"))

        if choose ==1:
            amount=int(input("Enter the Amount :"))
            amount= DepositAccount(user_name,user_Accno,balance_user,amount)
            new_balance = amount.Deposit1()
            balance_user = new_balance
            print(f"Deposited {amount}. New balance is {new_balance}.")
            
        elif choose ==2:
            withdrawAccount = int(input("Enter The Withdraw Amount : "))
            withdrawAccount1 = WithdrawAccount(user_name,user_Accno,balance_user,withdrawAccount)
            new_balance = withdrawAccount1.Withdraw1()
            balance_user = new_balance
            print(f"Withdrew {withdrawAccount}. New balance is {balance_user}.")

        elif choose ==3:
            amount1 = DisplayAccount(user_name,user_Accno,balance_user)
            amount1.Display1()
        
        elif choose ==4:
            print("Exiting...")
            break
        
        else:
            print("You Entered Number is Invalid Number !")
main()