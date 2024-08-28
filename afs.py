import random
import time

OPERATOR = ['+', '-', '/', '*']
MIN_OPERATOR = 3
MAX_OPERATOR = 12
TOTAL_PROBLEM = 10

def generate_problem():
    left = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    right = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    operator = random.choice(OPERATOR)

    # Generate the problem expression
    expr = f"{left} {operator} {right}"
    try:
        # Calculate the answer
        answer = eval(expr)
        # Handle floating-point precision for division
        if operator == '/':
            answer = round(answer, 2)
    except ZeroDivisionError:
        # Handle division by zero (although with random integers this might not occur)
        expr, answer = generate_problem()  # Recurse to generate a new problem

    return expr, answer

def main():
    wrong = 0
    input("Press Enter to start...")
    print("----------------------")

    start_time = time.time()

    for i in range(TOTAL_PROBLEM):
        expr, answer = generate_problem()
        while True:
            guess = input(f'Problem #{i + 1}: {expr} = ')
            try:
                # Check if user input is a number
                if float(guess) == answer:
                    break
                else:
                    wrong += 1
                    print("Incorrect. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    end_time = time.time()
    total_time = end_time - start_time

    print("---------------")
    print(f"Nice work! You finished in {total_time:.2f} seconds.")
    print(f"You got {wrong} wrong answers.")

if __name__ == "__main__":
    main()
