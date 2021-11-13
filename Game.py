import random

LEVEL = 0
NUMBER = 1
MAX = 2
MAX_TRIES = 3
MIN = 4

def showMenu ():
    print ("1. Easy")
    print ("2. Intermediate")
    print ("3. Advanced")
    print ("4. Expert")
    while True:
        level = input("Select your difficulty level: ")
        try:
            level = int(level)
        except:
            pass
        else:
            if 1 <= level <= 4:
                break
    return level

def selectLevel ():
    level = showMenu()
    if level == 1:
        number = random.randint(0, 100)
        max = 100
        max_tries = 20
    elif level == 2:
        number = random.randint(0, 200)
        max = 200
        max_tries = 30
    elif level == 3:
        number = random.randint(0, 300)
        max = 300
        max_tries = 40
    elif level == 4:
        number = random.randint(0, 400)
        max = 400
        max_tries = 50
    else:
        print("Invalid level. Choosing easy level...")
        number = random.randint(0, 100)
        max = 100
        max_tries = 20
    min = 0
    return [level, number, max, max_tries, min]

def chooseGuess ():
    while True:
        guess = input("Write your guess: ")
        try:
            guess = int(guess)
        except:
            pass 
        else: 
            if 0 <= guess <= game_data[MAX]:
                break
    return guess

def updateMin (guess, current):
    if current < guess:
        return guess
    return current

def updateMax (guess, current):
    if current > guess:
        return guess
    return current

def numberTries (value):
    if value > 1:
        return " tries"
    return " try"
    
def help ():
    hint = input("Do you require help? (Y/[N]): ")
    if str.upper(hint) == "Y":
        print("The number you are looking for is between " + str(updated_min) + " and " + str(updated_max))

game_data = selectLevel()
tries = 0
updated_min = 0
updated_max = game_data[MAX]

while True:
    print ("Guess a number bewteen 0 and " + str(game_data[MAX]) + ":")
    guess = chooseGuess()
    tries += 1
    score = []
    if tries > game_data[MAX_TRIES]:
        print("You have ran out of tries, the number was " + str(game_data[NUMBER]) + ".")
    else:
        print("You have " + str(game_data[MAX_TRIES] - tries) + numberTries(game_data[MAX_TRIES] - tries) + " left.")
    if guess < game_data[NUMBER]:
        print ("The number is a bit bigger than your guess, try again!")
        updated_min = updateMin(guess, updated_min)
        help()
    elif guess > game_data[NUMBER]:
        print("The number is a bit smaller than your guess, try again!")
        updated_max = updateMax(guess, updated_max)
        help()
    else:
        print("Congratulations! You guessed the number correctly in " + str(tries) + numberTries(tries) + ".")
        name = input("Please, introduce your name: ")
        score.append([name, game_data[LEVEL], tries])
        break