def first_unique_character(string: str) -> str:
    string=string.lower().strip()
    for c in string:
        if string.count(c) == 1:
            return c
        
    return ''
        
print(first_unique_character('amazing'))
