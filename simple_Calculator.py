#simple calculator\

def add_number(num1,num2):
    return num1+num2

def sub_number(num1,num2):
    return num1-num2
    
def mul_number(num1,num2):
    return num1*num2
    
def div_number(num1,num2):
    return num1/num2
    

while True:
    print(f'{'1.ADD NUMBER'} {'2.SUB NUMBER'} {'3.MULTI NUMBER'} {'4,DIV NUMBER'} {'5.EXIT'}')
    option = int(input('select the option -->'))

    if option == 5:
        exit('exiting program..!')

    if option in (1,2,3,4):
        num1 = int(input('ENTER THE FIRST NUMBER -->'))
        num2 = int(input('ENTER THE SECOND NUMBER -->'))
        if option== 1:
            print('result :',add_number(num1,num2))
        
        elif option ==2:
            print('result :',sub_number(num1,num2))

        elif option ==3:
            print('result :',mul_number(num1,num2))

        elif option ==4:
            print('result :',div_number(num1,num2))

        