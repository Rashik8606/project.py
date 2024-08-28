#expence tracker using function

expence={}
wallet=1000
while True:
    def add_expence():
        global wallet
        user_Name=input('enter your expence >')
        if user_Name in expence:
            print('is already exist!!')
            user_Amount=int(input('enter your amount >'))
            if user_Amount<=wallet:
                old_Amount=expence[user_Amount]
                expence[user_Amount]=user_Amount+old_Amount
                wallet=wallet-user_Amount
            else:
                print('expence exceed already the balance ')
        else:
            user_Amount=int(input('enter your balance >'))
            expence[user_Name]=user_Amount
            wallet=wallet-user_Amount

    def add_balance():
        print(wallet)
        
    def view_Expence():
    
        if not expence:
            print('is not here')
        else:
            for i,j in expence.items():
                print(i,j)
      
    def exit1():
        exit('exit')

    print('1.add expence | 2.add balance | 3.view expence | 4.exit')
    choice=int(input('select your option >'))


    if choice==1:
        add_expence()

    elif choice==2:
        add_balance()

    elif choice==3:
        view_Expence()

    elif choice==4:
        exit1()

    else:
        print('invalid number !!')

 
  
   