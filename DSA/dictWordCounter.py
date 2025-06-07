def wordCounter(string) -> None:
    string = string.lower().strip() # remove leading & trailing whitespaces
    wordCount = {}
    word: str = ""

    for c in string:
        if c == ' ':
            if word: # makes sure blank words are not counted
                wordCount[word] = wordCount.get(word, 0) + 1
                word = ""
        else:
            word += c

    if word: # count last word if any
        wordCount[word] = wordCount.get(word, 0) + 1

    for key, value in wordCount.items():
        print(f"{key}: {value}")



wordCounter(" hello world  Hello World   hello")
