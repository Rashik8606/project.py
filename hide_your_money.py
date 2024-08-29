row1=["😃","😃","😃"]
row2=["😃","😃","😃"]
row3=["😃","😃","😃"]
matrix = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

user_ask = input('where hide your money -->')
row_num = int(user_ask[0])
colum_num = int(user_ask[1])
selct_list=matrix[row_num-1]
selct_list[colum_num-1]="#"
print(f"{row1}\n{row2}\n{row3}")