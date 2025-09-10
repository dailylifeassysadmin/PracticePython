# Guessing Game One

# Exercise 9 (and Solution)
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
number_to_guess = random.randint(1, 10)
guess = None
# while guess != number_to_guess:
#     guess = int(input("Take a guess: "))
#     if guess < number_to_guess:
#         print("Too low! Try again.")
#     elif guess > number_to_guess:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You've guessed the number.")
# print("Thanks for playing!")


while True:
    guess = int(input("Take a guess: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
    
    if guess == number_to_guess:
        continue_game = input("Do you want to play again? (yes/no): ").lower()
        if continue_game == 'yes':
            number_to_guess = random.randint(1, 10)
            print("I'm thinking of a new number between 1 and 10.")
        else:
            print("Thanks for playing!")
            break
    # else:
#print("Thanks for playing!")


# End of the game
