def remove_LR_whitespace(string) -> str:
    return string.strip()

def remove_L_whitespace(string) -> str:
    return string.lstrip()

def remove_R_whitespace(string) -> str:
    return string.rstrip()

print(remove_LR_whitespace("     Welcome, user!        "))
print(remove_L_whitespace("     Welcome, user!"))
print(remove_R_whitespace("Welcome, user!         "))
