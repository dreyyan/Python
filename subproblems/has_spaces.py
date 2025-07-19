def has_spaces(string: str) -> bool:
    if string.count(' ') != 0:
        return True
    return False

print(has_spaces("watch "))