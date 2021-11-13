# guessthenumber

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/guessthenumber)
https://github.com/lauralardies/guessthenumber

Hemos resuelto un programa para terminal que va a escoger un número aleatoriamente, dependiendo del nivel escogido, el rango de los números a adivinar será mayor o menor. A continuación, le va a pedir al usuario que adivine este número. El usuario contará con un número determinado de intentos y además podrá recibir ayuda del sistema para adivinar dicho número. También puedes hacer que la IA juegue a adivinar el número y además, al salir del juego, se mostrará una tabla con los puntuajes grabados.

El diagrama de flujo que tenemos en nuestro código es el siguiente:

<br>
<img height="400" src="https://github.com/lauralardies/guessthenumber/blob/main/guessthenumber.jpg" />
<br>

```
import random

LEVEL = 0
NUMBER = 1
MAX = 2
MAX_TRIES = 3
MIN = 4
AI = 5
END_GAME = 6

def showMenu ():
    print ("1. Easy")
    print ("2. Intermediate")
    print ("3. Advanced")
    print ("4. Expert")
    print ("5. AI")
    print ("6. Exit")
    while True:
        level = input("Select your difficulty level: ")
        try:
            level = int(level)
        except:
            pass
        else:
            if 1 <= level <= 6:
                break
    return level

def selectLevel (level):
    if level == 5:
        level = random.randint(1,4)
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

def showScore(score):
    print ("Score table:")
    for score_item in score:
        print ("Player : " + score_item[0] + ", level: " + str(score_item[1]) + ", solved in " + str(score_item[2]) + numberTries(score_item[2]))

score =  []
while True:
    level = showMenu()
    if level == END_GAME:
        showScore(score)
        break
    game_data = selectLevel(level)
    tries = 0
    updated_min = 0
    updated_max = game_data[MAX]
    if level == AI:
        print("The level the AI is playing is level " + str(game_data[LEVEL]))
    while True:
        if level == AI:
            guess = random.randint(updated_min, updated_max)
            print ("AI chose " + str(guess))
        else:
            print ("Guess a number bewteen 0 and " + str(game_data[MAX]) + ":")
            guess = chooseGuess()
        tries += 1
        if tries > game_data[MAX_TRIES]:
            print("You have ran out of tries, the number was " + str(game_data[NUMBER]) + ".")
        else:
            print("You have " + str(game_data[MAX_TRIES] - tries) + numberTries(game_data[MAX_TRIES] - tries) + " left.")
        if guess == game_data[NUMBER]:
            print("Congratulations! You guessed the number correctly in " + str(tries) + numberTries(tries) + ".")
            if level == AI:
                name = "Artificial Intelligence"
            else:
                name = input("Please, introduce your name: ")
            score.append([name, game_data[LEVEL], tries])
            break
        else:
            if guess < game_data[NUMBER]:
                print ("The number is a bit bigger than your guess, try again!")
                updated_min = updateMin(guess, updated_min)
                if level != AI:
                    help()
            elif guess > game_data[NUMBER]:
                print("The number is a bit smaller than your guess, try again!")
                updated_max = updateMax(guess, updated_max)
                if level != AI:
                    help()
