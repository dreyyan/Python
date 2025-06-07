def find(string, toFind) -> int:
    return string.find(toFind)

def startsWith(string, prefix) -> bool:
    return string.startswith(prefix)

def endsWith(string, postfix) -> bool:
    return string.endswith(postfix)

print(find("watch", "ch"))
print(startsWith("hello there", "hello"))
print(endsWith("hello there", "there"))



