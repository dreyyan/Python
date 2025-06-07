def count(string, substr) -> int:
    return string.count(substr)

def fill(num, width) -> str:
    return num.zfill(width)

print(count("onomatopoeia", "o"))
print(fill("250", 5))
