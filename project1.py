import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input('enter num of players >')
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print('must be 2 or 4 ')
    else:
         print('invalid try')

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score)<max_score:

    for players_idx in range(players):
        print('\nplyers number ',players_idx+1,'turn has just stated\n')
        print('your total score is ',player_score[players_idx],'\n')
        current_score = 0

        while True:
            should_roll = input('would you like to roll (y)')
            if should_roll.lower()!='y':
               break
        
            value = roll()
            if value==1:
              print("you rolled a 1 turn done")
              current_score = 0
              break
            else:
                current_score+=value
                print('you rolled a ',value)

            print('you score is ',current_score)
          
        player_score[players_idx]+= current_score
        print('your total score is ',player_score[players_idx])
      
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print('player number',winning_idx +1,'is the winner with a score ',max_score) 




