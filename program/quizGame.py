# PROBLEM: Program a quiz game that allows the user to answer a # of questions depending on the
# user and evaluates the score
import random, os, time

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")  # Clear console

def quiz_game():
    # Store questions
    questions = [
        {
            "question": "What is the most abundant gas in Earth's atmosphere?",
            "choices": ["Oxygen", "Nitrogen", "Argon", "Hydrogen"],
            "correct_answer": "Nitrogen"
        },
        {
            "question": "Who was the first President of the United States?",
            "choices": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"],
            "correct_answer": "George Washington"
        },
        {
            "question": "What is the capital of Japan?",
            "choices": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
            "correct_answer": "Tokyo"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "choices": ["Oxygen", "Gold", "Osmium", "Ozone"],
            "correct_answer": "Oxygen"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "choices": ["Earth", "Jupiter", "Saturn", "Mars"],
            "correct_answer": "Jupiter"
        },
        {
            "question": "Which year did World War II end?",
            "choices": ["1941", "1945", "1939", "1950"],
            "correct_answer": "1945"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "choices": ["Nucleus", "Ribosome", "Mitochondria", "Endoplasmic Reticulum"],
            "correct_answer": "Mitochondria"
        },
        {
            "question": "Which programming language is known for its use in web development?",
            "choices": ["C++", "Python", "Java", "JavaScript"],
            "correct_answer": "JavaScript"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "choices": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
            "correct_answer": "Leonardo da Vinci"
        },
        {
            "question": "What is the longest river in the world?",
            "choices": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
            "correct_answer": "Nile River"
        }
    ]

    print("[ QUIZ GAME ]")
    while True:
        name = input("Enter your name: ").strip() # Prompt user to input name
        if name: # If name is not empty
            break
        clear_console()
        print("Invalid input, name cannot be empty.")
        time.sleep(2)

    while True:
        choice = input(f"Hello {name}, are you ready to start the quiz [y/n]?: ").lower() # Prompt user to start the quiz
        if choice == 'y':
            break
        elif choice == 'n':
            print(f"Goodbye {name}, have a nice day!")
            time.sleep(2)
            exit(0)
        else:
            print("Invalid input, please enter 'y' to start quiz or 'n' to exit the game.")
            time.sleep(2)

    while True:
        try:
            clear_console()
            question_count = int(input("Enter # of questions [max: 10]: "))
            if 1 <= question_count <= 10: # If # of questions is between 1-10
                break # Exit loop
            print("Invalid # of questions, please enter a value between 1-10.")
            time.sleep(2)
        except ValueError:
            print("Invalid # of questions, please enter a value between 1-10.")
            time.sleep(2)

    score = 0 # To store the player's current score
    asked_questions = set() # To track used questions

    for current_number in range(1, question_count + 1):
        while True:
            question = random.choice(questions) # Pick a random unique question
            if question["question"] not in asked_questions: # If question has not yet been asked
                asked_questions.add(question["question"]) # Set as an asked question
                break

        # Display formatted choices(A, B, C, D)
        formatted_choices = [f"{chr(65 + i)}.) {choice}" for i, choice in enumerate(question["choices"])]

        clear_console()
        # Display question and choices
        print(f"Question #{current_number}:") # Display Header
        print(question["question"]) # Display Question
        print("\n".join(formatted_choices)) # Display Choices

        # Prompt user for answer
        answer = input("Answer: ").strip()

        # Convert user answer to actual choice text
        answer_index = ord(answer.upper()) - 65  # Convert to ASCII ('A' -> 0, 'B' -> 1, etc.)
        if 0 <= answer_index < len(question["choices"]):
            user_choice = question["choices"][answer_index]
        else:
            user_choice = None  # Invalid letter (Letters except A-D)

        # Check correctness
        if user_choice ==   question["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect... The correct answer was: {question['correct_answer']}")

        # Clear console before the next question
        input("Press Enter to continue...")  # Pause before clearing
        clear_console()

    # End quiz and display results
    print(f"Quiz ended!\nTotal Questions: {question_count}\nTotal Score: {score}/{question_count}")

    choice = input("Play again[y/n]?: ").strip() # Ask user if he wants to start the quiz again
    if choice == 'y':
        quiz_game()
    elif choice == 'n':
        print("Thank you for playing!")
        time.sleep(2)
    else:
        print("Invalid choice, please enter 'y' to play again or 'n' to exit the game.")
        time.sleep(2)

# Run the game
quiz_game()