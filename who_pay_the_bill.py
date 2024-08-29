import random

name = input('Who Pay the bill > Enter the Name comma saperated -->')
name_list = name.split(',')
print(f'{random.choice(name_list)} You Will Pay')