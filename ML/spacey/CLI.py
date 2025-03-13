import importlib, os, time

from MathBot import initialize_mathbot


# UTILITY: Display error message
def error_message(error_message):
    character_delay_animation(f'[ ERROR: {error_message} ]', 0.025)

# UTILITY: Clear the console screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# UTILITY: Display text using delayed character-by-character output
def character_delay_animation(string_input, seconds):
    for char in string_input:
        print(char, end="")
        time.sleep(seconds)
    print()

# FUNCTION: Display the CLI
def display_command_line_interface():
    bots_list = ["mathbot"] # Store name of bots

    # / importlib / For dynamic function calling using module imports
    module = importlib.import_module("MathBot")

    while True:
        character_delay_animation("~`~`~`~`~`~`~`~` [ SmartCLI ] `~`~`~`~`~`~`~`~", 0.03)
        user_input = input(">> ")  # Prompt user to enter a command
        user_input = user_input.lower().strip()  # Convert to lowercase & remove whitespaces

        # Handle other cases
        if user_input not in bots_list: # Invalid command
            error_message("Unknown command, please try again")
            clear_screen()
        elif user_input == "exit": # Exit command
            exit(0)
        else: break

    command = "initialize_" + user_input # Concatenate user input for the function call
    getattr(module, command)()  # Call function dynamically

initialize_mathbot() # DEBUG
# display_command_line_interface() # Start