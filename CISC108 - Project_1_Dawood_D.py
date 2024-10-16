'''
Author: acbart (2/6/2019)
Version: 1
Co-author: ddawood (6/22/2021)

1. Give a brief description of how the code below works.
   Use plain, accessible language and avoid repeating
   the exact statements from the code. Aim to write at
   least 3 sentences.
   
   The guessing game starts off by asking the user their name, after the user inputs an answer,
   the rules of the game will be displayed and will ask the user to guess a number between a certain range.
   Once the user inputs a number, the code will either tell the user to go higher or lower or it would
   congratulate the user for guessing the correct number.
   ________________________________

2. Make a modification to the code in some place that changes the game
   in some interesting way. This cannot be as simple as changing the
   MINIMUM or one of the printed messages, but make enough changes and
   they can add up. You might allow the player to play more rounds after
   the first one, or completely change all the messages to have a pirate
   theme, or make it so the player can specify the maximum number.
   Describe your change here clearly and explain why you thought it was
   interesting.
   
   Changed guessing game to a Wizard theme, edited some of the responses
   the user will see as well as the minimum/maximum rnage. Created a new function
   that prompts the user to choose whether they'd like to play another round.
   If yes, game will restart and if no, then game will end by printing the ending
   message. I think these changes made the game more interesting to me as one of
   my favorite childhood games was Wizard101. Put a considerable amount of "^"
   where ever change was made.

'''

# Import the randint function generate random integers
from random import randint

# Establish the lower and uppper bound on the goal number
MINIMUM = 0
MAXIMUM = 125
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def print_welcome():
    '''
    Prompt the user for their name, and then display a
    simple message explaining the rules of the game.
    '''
    # Get the name of the user
    name = input("Enter your name? ")
    # Show the user's name 
    print("Hello wizard", name, "and welcome to my magical game.")
    # Print out the limits of the goal number
    print("I'm thinking of a number between", MINIMUM, "and", MAXIMUM)
    # Write out rest of the instructions 
    print("You need to use your magical intuition to guess that number.")
    print("I'll tell you if you need to go higher or lower.")
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def print_ending():
    '''
    Print out a conclusive message to wrap up the game.
    '''
    print("Nice job oh young wizard, see you next time!")
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
def process_guess(guess, goal):
    '''
    Print out whether or not the user was above, below,
    or at the goal.
    
    Args:
        guess (int): The number that the user entered
            as their guess.
        goal (int): The number that the computer is
            thinking of.
    '''
    # Branch execution based on whether the guess was right
    if guess < goal:
        print("Is that the best you can do? Go higher!")
    elif guess > goal:
        print("Is that the best you can do? Go lower!")
    else:
        print("Wonderful, it's", goal)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def get_number():
    '''
    Ask the user for a number, and keep prompting
    them until they give you an actual number
    (as opposed to giving you a letter).
    '''
    # Get the guess from the user, returns a string
    number = input("Enter guess? ")
    # Was the string composed only of numbers? ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    if number.isdigit():
        # If so, we can safely convert it to an integer
        number_as_int = int(number)
        # And return the result
        return number_as_int
    else:
        # Otherwise, call this function again recursively
        return get_number()
def play_again():
    '''
    Ask the user if they'd like to play another round
    by 0 = False and 1 = True. Once given an answer either
    continue new round or stop game.
    '''
    # Ask user whether they'd like to play again, prompt answer choices to 0 or 1
    playAgain = int(input("Do you want to play another round? If yes input 1, if no input 0:"))
    # If user chooses to play again, game will start fresh. If not, ending message will be printed
    if playAgain == 0:
        print_ending()
    elif playAgain == 1:
        main_game()
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def main_game():
    '''
    Play a round of the game.
    '''
    # Pick random number between MINIMUM and MAXIMUM
    goal = randint(MINIMUM, MAXIMUM)
    # Initially, the user hasn't guessed anything.
    user_guess = None

    print_welcome()
    # Repeatedly ask the user until they get it right
    while user_guess != goal:
        user_guess = get_number()
        process_guess(user_guess, goal)
    play_again()
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# This if statement is common in most professional Python
#   programs - don't worry too much about what it does,
#   but you can safely assume it will work when you press
#   the run button.
if __name__ == '__main__':
    main_game()