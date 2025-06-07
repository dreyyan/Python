import spacy

# Load spaCy's NLP model
nlp = spacy.load("en_core_web_sm")

# To-Do List storage
todo_list = []


def process_command(command):
    """Processes user input and executes the appropriate action."""
    doc = nlp(command.lower())  # Convert to lowercase and process with NLP

    if "add" in command or "new" in command:
        task = command.replace("add", "").replace("new", "").strip()
        if task:
            todo_list.append(task)
            return f"✅ Task added: {task}"
        return "Please specify a task to add."

    elif "remove" in command or "delete" in command:
        task = command.replace("remove", "").replace("delete", "").strip()
        if task in todo_list:
            todo_list.remove(task)
            return f"❌ Task removed: {task}"
        return "Task not found in the list."

    elif "show" in command or "view" in command or "list" in command:
        if todo_list:
            return "📋 Your To-Do List:\n" + "\n".join([f">> {task}" for task in todo_list])
        return "Your to-do list is empty."

    elif "clear" in command or "reset" in command:
        todo_list.clear()
        return "🗑️ To-Do List cleared!"

    elif "exit" in command or "quit" in command:
        return "Thank you for using ListBot!"

    else:
        return "I didn't understand that. Try commands like: 'add homework', 'remove shopping', 'show list'."


# AI Assistant Loop
print("🤖 ListBot: To-Do List Assistant\n(Type 'exit' to quit)")
while True:
    user_input = input("You: ")
    response = process_command(user_input)
    print("ListBot:", response)

    if "Goodbye" in response:
        break