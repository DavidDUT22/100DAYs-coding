# Number Guessing Game

import random

secret_number = random.randint(1, 50)
guess = 0
attempts = 0

print("I'm thinking of a number between 1 and 50.")

while guess != secret_number:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"You got it! The number was {secret_number}.")
        print(f"It took you {attempts} attempts.")