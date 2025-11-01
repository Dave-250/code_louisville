""" Create a Python program that plays a game of Rock, Paper, Scissors between a user and the computer. 
You’ll practice handling user input, generating random selections, and applying conditional logic.

Requirements
User Input

Prompt the user to enter 'rock', 'paper', or 'scissors'.
Convert the input to lowercase to standardize the comparison.

Add input validation: if the user enters anything other than 'rock', 'paper', or 'scissors', display an error message. (*hint - store the 
options in a list and check to see if user's input is in the list)

Computer Choice
Randomly select the computer’s choice from the same three options. (*hint: remember the random library. )

Game Logic
Compare the user’s choice to the computer’s choice.
If both choices are the same, print that it’s a tie.

Otherwise, apply the rules of the game:

Rock beats Scissors
  - Scissors beats Paper
- Paper beats Rock
  * Output
Display both the user’s and computer’s choices.
Clearly print the result: who won or if it was a tie.
"""
import random

def evaluate(computers_choice, users_choice, user_wins, computer_wins):
        """ Evaluate the winner.
        - Rock beats Scissors
        - Scissors beats Paper
        - Paper beats Rock
        """
        if computers_choice == 'rock' and users_choice == 'scissors':
            computer_wins += 1
            print("Computer wins")

        if computers_choice == 'rock' and users_choice == 'paper':
            user_wins += 1
            print("user wins")
        
        if computers_choice == 'scissors' and users_choice == 'rock':
            user_wins += 1
            print("User wins")

        if computers_choice == 'scissors' and users_choice == 'paper':
            computer_wins += 1
            print("Computer wins")
        
        if computers_choice == 'paper' and users_choice == 'scissors':
            user_wins += 1
            print("User wins")

        if computers_choice == 'paper' and users_choice == 'rock':
            computer_wins += 1
            print("computer wins")

        if computers_choice == users_choice:
            print("it's a tie!")

        if user_wins == 2:
            print(f"Congratulations user")
        elif computer_wins == 2:
            print("Congratulations bot")


count = 0
computer_wins = 0
user_wins = 0

choices = ['rock', 'paper', 'scissors']
while count < 3:
    count += 1
    # ask player for input
    users_choice = input(f"Choose one {choices}:").lower()

    if users_choice not in choices:
        print(f"Invalid choice! Please choose {choices}.")
        exit()

    # computer randomly chooses rock, paper, or scissors
    computers_choice = random.choice(['rock', 'paper', 'scissors']).lower()

    # determine winner
    result = evaluate(computers_choice, users_choice, user_wins, computer_wins)
    print(result)
