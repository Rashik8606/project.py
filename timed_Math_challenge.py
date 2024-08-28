import random 
import time
OPERATOR = ['+','-','/','*']
MIN_OPERATOR = 3
MAX_OPERATOR = 12
TOTAL_PROBLEM = 10

def generate_problem():
    left = random.randint(MIN_OPERATOR,MAX_OPERATOR)
    right = random.randint(MIN_OPERATOR,MAX_OPERATOR)
    operators = random.choice(OPERATOR)

    expr =str(left) + " " + operators +" " + str(right)
    answer = eval(expr)
    return expr,answer

wrong = 0
input("press enter to start...")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr,answer = generate_problem()
    while True:
        guess = input('problem #' +str(i+1) + ": " + expr +" = ")
        if guess == str(answer):
            break
        wrong +=1

end_time = time.time()
total_time = end_time-start_time
print("---------------")
print("Nice Work ! you finished in ",total_time,"seconds !")



