def word_counter(string: str) -> int:
    # remove leading/trailing whitespaces
    string=string.strip()

    word_count=len(string.split())
    return word_count
    
print(word_counter(" The quick  brown fox jumps over the  fence. "))