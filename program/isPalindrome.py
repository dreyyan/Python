print("Palindrome Checker")

word = input("Enter Word: ")
reversed_word = ""
counter = -1

while True:
    reversed_word += word[counter]

    if len(word) == len(reversed_word):
        if word == reversed_word:
            print(str(word) + " is a palindrome")
            break

        else:
            print(str(word) + " is not a palindrome")
            break
    else:
        counter -= 1