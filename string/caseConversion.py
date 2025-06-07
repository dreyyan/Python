def toUppercase(string) -> str:
    return string.upper()

def toLowercase(string) -> str:
    return string.lower()

def capitalize(string) -> str:
    return string.capitalize()

def capitalizeAll(string) -> str:
    return string.title()

print(f"{toUppercase("the quick brown fox jumps over the fence")}")
print(f"{toLowercase("THE QUICK BROWN FOX JUMPS OVER THE FENCE")}")
print(f"{capitalize("steve")}")
print(f"{capitalizeAll("the book of life")}")
