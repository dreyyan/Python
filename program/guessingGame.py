# PROBLEM: Program a guessing game that allows the user to enter the desired difficulty, and lets the user
# guess the number until the user guesses the correct number or the # of attempts reach zero
import os, random, time
# FUNCTION: Display line format
def display_format(length):
    for _ in range(length):
        print('-', end="")
    print()

# FUNCTION: Clear the console screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def start_game():
    while True:
        clear_screen()
        difficulty = "" # To store the difficulty
        attempts = 5 # Set default attempts
        range = 5 # Set maximum range for random number

        # Display difficulties
        print("[ DIFFICULTY ]")
        display_format(14)
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        display_format(14)

        try:
            difficulty_choice = int(input("Enter difficulty: ").strip()) # Prompt user to enter the desired difficulty

            if difficulty_choice == 1:  # Difficulty - Easy
                difficulty = "easy"
            elif difficulty_choice == 2:  # Difficulty - Medium
                difficulty = "medium"
                attempts = 4
                range = 10
            elif difficulty_choice == 3:  # Difficulty - Hard
                difficulty = "hard"
                attempts = 3
                range = 15
            else:
                print("Invalid difficulty, please enter a valid difficulty(1-3).")
                time.sleep(2)
        except ValueError:
            print("Invalid difficulty, please enter a valid difficulty(1-3).")
            time.sleep(2)
            difficulty = ""

        if difficulty != "":  # If set difficulty
            break # Exit loop

    random_number = random.randint(1, range) # Generate random number
    attempts_used = 0 # To store the attempts used
    game_won = False # To check if player won the game

    # Let user guess the number until # of attempts are zero
    while attempts != 0:
        clear_screen()
        if attempts != 1:
            print(f"[{attempts} attempts]")
        else:
            print(f"[{attempts} attempt]")
        guess = int(input(f"Guess the number[1 - {range}]: "))
        if guess > range or guess < 1: # If guess exceeds the range
            print(f"Invalid guess, only guess values between 1 and {range}.")
            time.sleep(2)
        elif guess == random_number: # If number was guessed correctly
            game_won = True
            print(f"You guessed it! The number was: {random_number}")
            time.sleep(2)
            print(f"You guessed it in: {attempts_used} attempt/s")
            time.sleep(2)
            break
        else:
            attempts_used += 1 # Increment attempts used
            attempts -= 1 # Decrement the attempts left
            if guess > random_number: # If guess is too high
                print("Too high!")
                time.sleep(2)
            elif guess < random_number: # If guess is too low
                print("Too low!")
                time.sleep(2)

    clear_screen()
    if not game_won: # If player lost the game
        print(f"You lost... the number was: {random_number}")
    # Prompt user to play again or exit the game
    end_choice = input("Play again[y/n]?: ").lower().strip()
    if end_choice == 'y':
        start_game()
    else:
        print("Thank you for playing!")
        exit(0) # Exit game

while True:
    try:
        clear_screen()
        # Prompt user to start the game or exit
        print("[ GUESSING GAME ]")
        display_format(17)
        print("1. Start")
        print("2. Exit")
        display_format(17)
        user_choice = int(input("Enter choice: ").strip())  # Prompt user to enter a choice
    except ValueError:
        print("Invalid choice, please enter '1' to start or '2' to exit.")
        time.sleep(2)
    else:
        if user_choice == 1:  # Start the game
            start_game()
        elif user_choice == 2:  # Display exit message
            print("Thank you for playing!")
            time.sleep(1)
            exit(0)  # Exit the game
        else:
            print("Invalid choice, please enter '1' to start or '2' to exit.")
            time.sleep(2)