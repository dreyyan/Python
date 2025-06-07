def removeLRWhitespace(string) -> str:
    return string.strip()

def removeLWhitespace(string) -> str:
    return string.lstrip()

def removeRWhitespace(string) -> str:
    return string.rstrip()

print(removeLRWhitespace("     Welcome, user!        "))
print(removeLWhitespace("     Welcome, user!"))
print(removeRWhitespace("Welcome, user!         "))
