name1 = input('enter your name --->')
name2 = input('enter him/her name --->')
combine_Name = name1 + name2
lower_String = combine_Name.lower()

t = lower_String.count('t')
r = lower_String.count('r')
u = lower_String.count('u')
e = lower_String.count('e')
true = t+r+u+e

l = lower_String.count('l')
o = lower_String.count('o')
v = lower_String.count('v')
e = lower_String.count('e')
love = l+o+v+e

convert_string = int(str(true)+str(love))
if convert_string <10 or convert_string >90:
    print(f"your score is {convert_string} and you go together like coke and mentos ")
elif convert_string >=40 and convert_string <=50:
    print(f"your score is {convert_string} and your alright together")
else:
    print(f"your love is {convert_string}")


