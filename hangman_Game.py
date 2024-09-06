import random
chose_display = ['apple','orange','potato']
live = 6
display = random.choice(chose_display)
print(display)
empty_lis = []
for i in range(len(display)):
    empty_lis += "_"
print(empty_lis)
game_Over = False
while not game_Over:
    user_input = input("Guess a Letter :").lower()
    for i in range(len(display)):
        letter = display[i]
        if letter == user_input:
            empty_lis[i]=user_input
    print(empty_lis)
    if user_input not in display:
        live -=1
        if live == 0:
            game_Over = True
            print("You Lose !")

    if "_" not in empty_lis:
        game_Over = True
        print("You Win")