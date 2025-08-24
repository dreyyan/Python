def replace_to(string, old, new) -> str:
    return string.replace(old, new)

def split(string, sep) -> str:
    return string.split(sep)

def join(lst, connector) -> str:
    return connector.join(lst)

print(replace_to("hippopotamus", 'po', 'ap'))
print(split("i am a great programmer", ' '))
print(join(["we", "are", "the", "champions"], ' '))
