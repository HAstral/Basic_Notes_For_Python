import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a num between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess< lowest_num or guess> highest_num:
            print("That num is out of range")
            print(f"Just select a num between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Answer again.")
        elif guess > answer:
            print("Too high! Answer again.")
        else:
            print(f"CORRECT! The answer is {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Just select a num between {lowest_num} and {highest_num}")
