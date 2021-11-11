import random

max = "100"
updated_min = 0
updated_max = max 


def showMenu ():
    print("Select your difficulty level:")
    print("  1. Easy")
    print("  2. Intermediate")
    print("  3. Advanced")
    print("  4. Expert")

    level = int(input())
    return level

def updateMin (guess, current):
    if current < guess:
        return guess
    return current

def updateMax (guess, current):
    if current > guess:
        return guess
    return current

level = showMenu()

if level == 1:
    number = random.randint(0,100)
    max = 100
    max_tries = 20
elif level == 2:
    number = random.randint(0,200)
    max = 200
    max_tries = 30
elif level == 3: 
    number = random.randint(0,300)
    max = 300
    max_tries = 40
elif level == 4:
    number = random.randint(0,400)
    max = 400
    max_tries = 50
else:
    print("Invalid level. Choosing easy level")
    number = random.randint(0,100)
    max = 100
    max_tries = 20

updated_max = max

print("Guess a number between 0 and " + str(max) + ":")
guess = int(input("Write your guess: "))
tries = 1

while guess != number:
    if tries == max_tries:
        print ("You have ran out of tries. The number was " + str(number))
        break
    else:
        print ("You have " + str(max_tries - tries) + " tries left")
    if guess >= 0 and guess <= max:
        if guess > number: 
            print("The number is a bit smaller than your guess, try again!")
            updated_max = updateMax(guess, updated_max)
        elif guess < number:
            print("The number is a bit bigger than your guess, try again!")
            updated_min = updateMin(guess, updated_min)
        hint = input("Do you require help? (Y/[N]): ")
        if str.upper(hint) == "Y":
            print ("The number is between " + str(updated_min) + " and " + str(updated_max))
        print("Guess a number between 0 and " + str(max) + ":")
        guess = int(input("Write your guess: "))
        tries = tries + 1
    else:
        print("Guess a number between 0 and " + str(max) + ":")
        guess = int(input("Write your guess: "))

if guess == number:
    sTries = " try."
    if tries > 1:
        sTries = " tries."
    print("Congratulations! You guessed the number correctly in " + str(tries) + sTries)