name1 = input('enter your name -->')
name2 = input('enter him/her name -->')
combine_Name = name1 + name2
conver_Name = combine_Name.lower()

def count_Letters(letters, string):
    count = 0
    for letter in letters:
        count += string.count(letter)
    return count

letters_Count = 'true'
true_Score = count_Letters(letters_Count, conver_Name)

love_letter = 'love'
true_Love = count_Letters(love_letter, conver_Name)

convert_string = int(f"{true_Score}{true_Love}")

if convert_string <10 or convert_string >90:
    print(f"Your score is {convert_string} and you go together like coke and mentos.")
elif 40<= convert_string <=50: 
    print(f"Your score is {convert_string} and you're alright together.")
else:
    (f"Your love is {convert_string}.")

        