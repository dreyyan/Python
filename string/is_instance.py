def is_digit(string) -> bool:
    return string.isdigit()

def is_alpha(string) -> bool:
    return string.isalpha()

def is_alnum(string) -> bool:
    return string.isalnum()

print(is_digit("12345"))
print(is_alpha("Abcde"))
print(is_alnum("12345Abcde"))
