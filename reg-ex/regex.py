import re

# [ 1 | re.search ] checks for first match in the string
def search_for(string, word) -> bool:
    match = re.search(word, string)
    
    if match:
        return True if match else False
    
    return False

print(search_for("The quick brown fox", "fox"))

# [ 2 | re.match ] checks if matching first word
def word_starts(string, word) -> bool:
    match = re.match(word, string)

    return True if match else False

print(word_starts("Coding is awesome!", "Coding"))

# [ 3 | re.findall ] checks for all matches
def search_all(string) -> list:
    match = re.findall(r"\d{3}-\d{3}-\d{4}", string)
    return match

print(search_all("123-456-7890, 987-654-3210"))

# [ 4 | re.sub ] replaces match with new text
def replace_to(string) -> None:
    newText = re.sub(r"\d{4}", "2024", string)
    print(newText)

replace_to("Next year is 2026.")
