def is_palindrome(string: str) -> bool:
    palindrome:str = string[::-1]

    if string==palindrome:
        return True
    return False
print(is_palindrome('racecar'))
    