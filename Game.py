import random

number = random.randint(0,99)

print(number)

print("Guess a number between 0 and 99:")
guess = input("Write your guess:")

while guess != number:  
    if guess > str(number): 
        print("The number is a bit lower than your guess, try again!")
        print("Guess a number between 0 and 99:")
        guess = input("Write your guess:")
    elif guess < str(number):
        print("The number is a bit higher than your guess, try again!")
        print("Guess a number between 0 and 99:")
        guess = input("Write your guess:")
print("Congratulations! You guessed the number correctly.")