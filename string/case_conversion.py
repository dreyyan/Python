def to_uppercase(string) -> str:
    return string.upper()

def to_lowercase(string) -> str:
    return string.lower()

def capitalize(string) -> str:
    return string.capitalize()

def capitalize_all(string) -> str:
    return string.title()

print(f"{to_uppercase("the quick brown fox jumps over the fence")}")
print(f"{to_lowercase("THE QUICK BROWN FOX JUMPS OVER THE FENCE")}")
print(f"{capitalize("steve")}")
print(f"{capitalize_all("the book of life")}")
