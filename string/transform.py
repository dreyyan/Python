def replaceTo(string, old, new) -> str:
    return string.replace(old, new)

def split(string, sep) -> str:
    return string.split(sep)

def join(lst, connector) -> str:
    return connector.join(lst)

print(replaceTo("hippopotamus", 'po', 'ap'))
print(split("i am a great programmer", ' '))
print(join(["we", "are", "the", "champions"], ' '))
