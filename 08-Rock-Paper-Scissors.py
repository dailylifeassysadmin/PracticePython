# Rock Paper Scissors
# Exercise 8 (and Solution)
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

def rps_game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        player1 = input("Player 1, enter your choice (rock, paper, scissors): ").lower()
        player2 = input("Player 2, enter your choice (rock, paper, scissors): ").lower()

        if player1 == player2:
            print("It's a tie!")
        elif (player1 == 'rock' and player2 == 'scissors') or \
             (player1 == 'scissors' and player2 == 'paper') or \
             (player1 == 'paper' and player2 == 'rock'):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
#rps_game()

print("Welcome to the Rock-Paper-Scissors game!")

while True:
    player1 = input("Player 1, enter your choice (rock, paper, scissors): ").lower()
    player2 = input("Player 2, enter your choice (rock, paper, scissors): ").lower()

    if player1 not in ['rock', 'paper', 'scissors'] or player2 not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    if player1 == player2:
        print("It's a tie!")
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'scissors' and player2 == 'paper') or \
         (player1 == 'paper' and player2 == 'rock'):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

# End of program.