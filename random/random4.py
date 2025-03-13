import random
ans = random.uniform(1,100)
guess = 0

while not guess == ans:
    guess = float(input("Guess a number please: "))
    if guess > ans:
        print("Too high, try again")
    elif guess < ans:
        print("Too low, try again")
    elif guess == ans:
        print("Well done, you are amazing")
    else:
        print("What how did you get here you hacker")