number = 21
guess = ""

while (guess != number):
    guess = int(input("Guess the number: "))
    if guess < number:
        print("Higher!")

    elif guess > number:
        print("Lower!")

    else:
        print("You guessed it! the number was " + str(number) + "!")