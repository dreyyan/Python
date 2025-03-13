import random
import os

attempts = 0
guess = 0

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

# Set end range and # of attempts
while True:
    # Prompt user to enter difficulty
    print("Difficulty:")
    difficulty_choice = int(input("[1] | Easy\n[2] | Medium\n[3] | Hard\n>> ").strip())

    # Check for difficulty choice and assign values based on difficulty
    if difficulty_choice == 1:
        end_range = 10
        attempts = 5
        break
    elif difficulty_choice == 2:
        end_range = 20
        attempts = 4
        break
    elif difficulty_choice == 3:
        end_range = 30
        attempts = 3
        break
    else:
        print("[ ERROR | Invalid choice ]")

# Set range of values
number = random.randint(1, end_range)

# Let user guess the number
while guess != number:
    # Break if no more attempts
    if attempts == 0: break
    guess = int(input(f"Guess[1 - {end_range}]: "))
    clear_console()
    if guess < number:
        print("guess is too low...")
        attempts -= 1
        print(f"{attempts} attempts left!")
    elif guess > number:
        print("guess is too high...")
        attempts -= 1
        print(f"{attempts} attempts left!")
    else:
        print("You guessed it! the number was: " + str(number) + "!")
        exit(0)

# Display if number wasn't guessed correctly
print(f"Too close! The number was...{number}!\nBetter luck next time...")