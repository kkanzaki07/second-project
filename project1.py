import random
import time

OPERANTS = ['+', '-', '*']
MIN_NUMBER = 0
MAX_NUMBER = 20
TOTAL_PROBLEMS = 20

def problems():
    left = random.randint(MIN_NUMBER, MAX_NUMBER)
    right = random.randint(MIN_NUMBER, MAX_NUMBER)
    operant = random.choice(OPERANTS)

    expr = str(left) + " " + operant + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Enter to start!")
print("-----------------")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = problems()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong =+ 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("-----------------")
print("GG you finished in " + str(total_time) + " seconds and with " + str(wrong) + " wrong answers!!!!!!")
