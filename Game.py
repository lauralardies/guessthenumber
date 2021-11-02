import random

number = random.randint(0,99)

print("Guess a number between 0 and 99:")
guess = int(input("Write your guess: "))
tries = 1

while guess != number:
    if guess >= 0 and guess <= 99:
        if guess > number: 
            print("The number is a bit smaller than your guess, try again!")
        elif guess < number:
            print("The number is a bit bigger than your guess, try again!")
        print("Guess a number between 0 and 99:")
        guess = int(input("Write your guess: "))
        tries = tries + 1
    else:
        print("Guess a number between 0 and 99:")
        guess = int(input("Write your guess: "))

sTries = " try."
if tries > 1:
    sTries = " tries."
print("Congratulations! You guessed the number correctly in " + str(tries) + sTries)