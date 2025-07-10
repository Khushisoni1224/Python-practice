# File: number_guessing_game.py
# Number guessing game with 3 chances
# Random number between 1–20

import random
x = random.randint(1, 20)
a = int(input("Guess a number (1–20): "))

for i in range(3):
    if a == x:
        print("You guessed it! ")
        break
    elif i == 0:
        print("2 chances left")
    elif i == 1:
        print("1 chance left")
    else:
        print("You lost! The number was:", x)
    a = int(input("Try again: "))