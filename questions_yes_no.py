questions = [
     {
        'prompt': 'IN WHAT YEAR DID THE GREAT OCTOBER SOCIALIST REVOLUTION TAKE PLACE ?',
        'option': ['A.1917', 'B.1923', 'C.1914', 'D.1920'],
        'answer': 'A'
    },
    {
        'prompt': 'WHICH PLANET IN THE SOLAR SYSTEM IS KNOW AS THE RED PLANET ?',
        'option': ['A.venum', 'B.earth', 'C.mars', 'D.jupiter'],
        'answer': 'C'
    },
    {
        'prompt': 'WHAT IS THE CAPITAL OF JAPAN',
        'option': ['A.BEIJIN', 'B.TOKYO', 'C.SEOUL', 'D.BANGKOK'],
        'answer': 'B'
    }

    
]

def ans_Qus(questions):
    score=0
    for question in questions:
        print(question['prompt'])
        for option in question['option']:
            print(option)

        user=input('enter the correct answer> ?').upper()
        if user==question['answer']:
            print('you entered correct answer')
            score+=1

        else:
            print('your loser !!incorrect answer')
    print(f'you got {score} out of {len(questions)} qustion corrct')

ans_Qus(questions)
    
 
     
