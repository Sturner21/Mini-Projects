print("Welcome to Guess the Number!")
print("You have six tries to guess the right number!")

import random

r_numb = random.randint(1, 20)

for i in range(6):
    guess = input("Take a guess: ")
    guess = int(guess)

    if guess < r_numb:
        print("That guess was a too low.")
    elif guess > r_numb:
        print("That guess was a too high.")
    elif guess == r_numb:
        break

if guess == r_numb:
    print("Congrats! You guess the right number!")

if guess != r_numb:
    print("Sorry, but you lost. The number that I was thinking of was {}.".format(r_numb))