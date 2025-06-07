def isDigit(string) -> bool:
    return string.isdigit()

def isAlpha(string) -> bool:
    return string.isalpha()

def isAlNum(string) -> bool:
    return string.isalnum()

print(isDigit("12345"))
print(isAlpha("Abcde"))
print(isAlNum("12345Abcde"))
