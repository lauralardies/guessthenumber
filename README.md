# guessthenumber

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/guessthenumber)
https://github.com/lauralardies/guessthenumber

Hemos resuelto un programa para terminal que va a escoger un número aleatoriamente, entre 0 y 99, y a continuación, le va a pedir al usuario que adivine este número.
El diagrama de flujo que tenemos en nuestro código es el siguiente:

![Figma](/lauralardies/guessthenumber/guessthenumber.jpg)

```import random

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
