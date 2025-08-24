def find(string, toFind) -> int:
    return string.find(toFind)

def starts_with(string, prefix) -> bool:
    return string.startswith(prefix)

def ends_with(string, postfix) -> bool:
    return string.endswith(postfix)

print(find("watch", "ch"))
print(starts_with("hello there", "hello"))
print(ends_with("hello there", "there"))



