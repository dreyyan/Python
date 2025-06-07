def groupLength(lst) -> None:
    wordsByLength = {}

    for word in lst:
        length = len(word)

        if length not in wordsByLength:
            wordsByLength[length] = [word]
        else:
            wordsByLength[length].append(word) 

    for key, value in wordsByLength.items():
        print(f"{key}: {value}")

lst = ['cat', 'ocean', 'dog', 'river', 'goat']
groupLength(lst)
