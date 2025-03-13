import random
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")  # Clear console

def quiz_game():
    print("[ Quiz Game ]|")

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

    # User input: Name
    while True:
        name = input("Enter your name: ").strip()
        if name: # If name is not empyu
            break
        clear_console()
        print("[ ERROR | Name cannot be empty ]") 

    # Confirm user to start quiz
    while True:
        choice = input(f"Hello {name}, are you ready to start the quiz [y/n]?: ").lower()
        clear_console()
        if choice == 'y':
            break
        elif choice == 'n':
            print(f"Goodbye {name}, have a nice day!")
            exit(0)

    # User input: # of questions
    while True:
        try:
            question_count = int(input("Enter # of questions [max: 10]: "))
            if 1 <= question_count <= 10: # Question count must be between 1-10
                break  # Valid number
            print("[ ERROR | Invalid number of questions ]")
        except ValueError:
            print("[ ERROR | Invalid input ]")
        clear_console()

    # Initialize score and question counter
    score = 0
    asked_questions = set()  # To track used questions

    # Quiz loop
    for current_number in range(1, question_count + 1):

        # Pick a random unique question
        while True:
            question = random.choice(questions)
            if question["question"] not in asked_questions:
                asked_questions.add(question["question"]) # Add question to asked questions set
                break

        # Format choices with A, B, C, D
        formatted_choices = [f"{chr(65 + i)}.) {choice}" for i, choice in enumerate(question["choices"])]

        clear_console()
        # Display question and choices
        print(f"Question #{current_number}:\n") # Display Header
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

# Run the game
quiz_game()