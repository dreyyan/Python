import os, time, spacy, operator
from word2number import w2n

# UTILITY: Display text with a typing effect
def character_delay_animation(string_input, seconds):
    for char in string_input:
        print(char, end="", flush=True)
        time.sleep(seconds)
    print()

# FUNCTION: Display bot response
def response(bot_response):
    character_delay_animation(f"[MathBot]: {bot_response}", 0.03)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def initialize_mathbot():
    character_delay_animation("[SMARTY]: Initializing MathBot...", 0.03)
    time.sleep(1)
    clear_screen()
    nlp = spacy.load("en_core_web_sm")

    character_delay_animation("* - * - * - * - * [ MathBot ] * - * - * - * - *", 0.03)

    operations = {
        "+": ["plus", "add", "addition", "sum"],
        "-": ["minus", "subtract", "subtraction", "difference"],
        "*": ["times", "multiply", "multiplication", "product"],
        "/": ["divide", "over", "division"]
    }

    operation_functions = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    while True:
        user_input = input("[You]: ").lower().strip()
        if user_input in ["exit", "quit"]:
            response("Goodbye!")
            break

        doc = nlp(user_input)
        numbers = []
        operation = None

        # Extract numbers
        for token in doc:
            try:
                if token.like_num:
                    numbers.append(w2n.word_to_num(token.text))
            except ValueError:
                continue  # Ignore invalid numbers

        # Detect operation
        for token in doc:
            for op, keywords in operations.items():
                if token.text in keywords:
                    operation = op
                    break
            if operation:
                break

        if not operation:
            response("Sorry, I did not recognize a valid operation.")
            continue

        response(f"I will perform {operations[operation][2]} for you...")

        if len(numbers) < 2:
            response("Please provide at least two numbers.")
            continue

        x, y = numbers[:2]
        if operation == "/" and y == 0:
            response("Division by zero is not allowed.")
        else:
            result = operation_functions[operation](x, y)
            response(f"{x} {operation} {y} is equal to {result}.")
