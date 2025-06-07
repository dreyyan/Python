def wordCounter(string) -> int:
    string = string.split()
    return len(string)
    
print(wordCounter("  the quick brown fox  jumps over  the fence. "))
