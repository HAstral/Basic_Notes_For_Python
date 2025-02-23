import random

options = ("rock", "paper" , "scissors")
print("Do you want to play a game? ")
ans=input("Enter (Y/N):").lower()
while ans == "y":
    opt=random.choice(options)
    guess=input("Enter your guess: ").lower()
    while guess in options:
        print(f"Player's choice is {guess}")
        print(f"Computer's choice is {opt}")
        if opt == "rock" and guess == "paper":
            print("Player Win!!")
        elif opt == "rock" and guess == "scissors":
            print("Computer Win!!")
        elif opt == "paper" and guess == "scissors":
            print("Player Win!!")
        elif opt == "paper" and guess == "rock":
            print("Computer Win!!")
        elif opt == "scissors" and guess == "rock":
            print("Player Win!!")
        elif opt == "scissors" and guess == "paper":
            print("Computer Win!!")
        else: 
            print("DRAW!!")
        break
    print("Do you want to play again?:")
    ans=input("Enter (Y/N):").lower()
