from random import random

print("I'm thinking of a number between 0 and 100")
number = int(random() * 100)

guesses = 0
guess = None
while guess != number:
    guess = input("Guess: ")
    if not guess.isnumeric():
        print("Your guess needs to be a number, silly!")
        continue
    guess = int(guess)
    if guess < 0 or guess > 100:
        print("Your guess needs to be between 0 and 100!")
        continue
    guesses += 1
    if guess < number:
        print("Your guess is too low!")
    if guess > number:
        print("Your guess is too high!")
    if guess == number:
        print(f"YAY! you got it right. It took you {guesses} guesses")
