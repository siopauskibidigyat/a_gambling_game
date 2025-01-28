#Python Slot Machine

import random
import os

def spin_row():
    symbols = ['🍒', '🍉', '🔔', '⭐']

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒': 
            return bet * 5
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0 

def save_progress(balance):
    with open("slot_save.txt", "w") as f:
        f.write(str(balance))

def load_progress():
    if os.path.exists("slot_save.txt"):
        with open("slot_save.txt", "r") as f:
            return int(f.read())
    return 1000       

def main ():
    balance = load_progress()
    free_spins = 0
    total_spins = 0
    total_bets = 0
    total_payouts = 0

    print("-----------------------")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🔔 ⭐ ")
    print("-----------------------")

    while balance > 0 or free_spins > 0:
        if free_spins > 0:
            print(f"You have {free_spins} free spin(s) remaining")
            bet = 0
            free_spins -= 1
        else:    
            print(f"Current balance : ${balance}")
            bet = input("Place your bet amount: ")

            if not bet.isdigit():
                print("-Please enter a valid number-")
                continue

            bet = int(bet)

            if bet > balance:
                print("-Insufficient funds-")
                continue

            if bet <= 0:
                print("-Bet mus be greater than 0-")
                continue

            balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
            balance += payout
        else:
            print("Sorry, you lost")
            print("Better luck next time!")

        if row[0] == row[1] == row[2]:
            print(f"You hit three {row[0]}! You also won 10 free spins!")
            free_spins += 10
        
        total_spins +=1
        total_bets += bet
        total_payouts += payout     

        if free_spins == 0:  
            play_again = input("Do you want to spin again? (Y/N): ").upper()
            if play_again != 'Y':
                break
        else:
            play_again = input("Do you want to use your free spin? (Y/N): ").upper()
            if play_again != 'Y':
                break

    print("********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("********************************************")
    print("Game Summary:")
    print(f"Total games played: {total_spins}")
    print(f"Total bets placed: ${total_bets}")
    print(f"Total payouts received: ${total_payouts}")

    save_progress(balance)

if __name__ == '__main__':
    main()