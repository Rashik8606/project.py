print('PIZZA > SMALL RS.100 | MEDIUM RS.200 | LARGE RS,300')
select_Pizza = input('SELECT YOUR ORDER (S > M > L)--->')
bill = 0
if select_Pizza == 'S' or select_Pizza == 's':
    bill+=100
    print('SMALL PIZZA PRIZE 100 RS')
elif select_Pizza == 'm' or select_Pizza == 'M':
    bill+=200
    print('MEDIUM PIZZA PRIZE 200')
else:
    bill+=300
    print('LARGE PIZZA PRIZE 300 RS')

select_Pepperonni = input('DO YOU WANT MACARONNI (YES OR NO)-->')
if select_Pepperonni == 'YES' or select_Pepperonni == 'yes':
    if select_Pizza == 'yes' or select_Pizza=='YES':
        bill+=30
    else:
        bill+=50

select_Cheese = input('DO YOU WANT EXTRA CHEESE (YES OR NO )--->')
if select_Pizza == 'YES' or select_Pizza == 'yes':
    bill +=20

print('YOUR FINAL BILL',bill)