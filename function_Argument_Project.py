print("1.WITH ARGUMENT WITH RETURN| 2.WITH ARGUMENT WITHOUT RETURN| 3.WITHOUT ARGUMENT WITH RETURN| 4.WITHOUT ARGUMENT WITHOUT RETURN| 5.EXIT")
while True:
    user=int(input('SELECT YOUR OPTION -->'))
    if user==1:
        number=int(input('ENTER FIRST NUMBER-->'))
        number2=int(input('ENTER SECOND NUMBER-->'))
        def num(number,number2):
            result=number+number2
            return result
        result=num(number,number2)
        print('YOUR RESULT IS >',result)

    elif user==2:
        number=int(input('ENTER FIRST NUMBER-->'))
        number2=int(input('ENTER SECOND NUMBER-->'))
        def num(number,number2):
            s=number+number2
            result=s
            print('YOUR RESULT >',result)  
        num(number,number2)
        

    elif user==3:
        number=int(input('ENTER FIRST NUMBER-->'))
        number2=int(input('ENTER SECOND NUMBER-->'))
        def num():
            result=number+number2
            return result
        print('YOUR RESULT >',num())

    elif user==4:
        number=int(input('ENTER FIRST NUMBER-->'))
        number2=int(input('ENTER SECOND NUMBER-->'))
        def num():
            s=number+number2
            result=s
            print('YOUR RESULT >',result)
        num()
    else:
        exit('EXITED')
   
        
   
    