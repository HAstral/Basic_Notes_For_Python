import random
import time

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("************************")
    print(" | ".join(row))
    print("************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 5
        elif row[0] == '⭐':
            return bet * 10
    return 0

def main():
    balance = 100

    print("************************")
    time.sleep(0.5)
    print("Welcome to the Slot Machine")
    time.sleep(0.5)
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")  # to get emojis, press windows + . (dot)
    time.sleep(0.5)
    print("************************")
    time.sleep(0.5)

    while balance > 0:
        print(f"Current balance: ${balance}")
        time.sleep(0.5)

        bet = input("Place your bet: ")
        if not bet.isdigit():
            print("Enter a valid bet")
            time.sleep(0.5)
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance")
            time.sleep(0.5)
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            time.sleep(0.5)
            continue
        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        time.sleep(0.5)
        print_row(row)
        time.sleep(0.5)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost")
        time.sleep(0.5)

        balance += payout
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break
    print("************************")
    print(f"Game Over! Your balance is ${balance:.2f}")
    print("************************")

if __name__ == "__main__":
    main()