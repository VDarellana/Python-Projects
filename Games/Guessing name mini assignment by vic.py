# UNIT 2: Mini Programming Project - Number Guessing Game
#
# Purpose to program the childhood game hi-low.  The computer picks
# a number between 1-100 and the human player tries to guess the number
# in the fewest number of rounds.  The game should keep track of how
# many attempts the player makes guessing the right number.
# Should the player take ten attempts at guessing the game ends displaying
# the correct answer and asks the user if they want to play again.
#
# Author: Victor Daniel Arellana Assia
#
# Date: DATE SUBMITTED HERE

# Setup the environment
import random                   # the library 'tool' used to generate pesudo random values
number = random.randint(1,100)  # pick a random value between 1 and 100
data = "NA"                     # the user's data to check valid input of whole numbers
counter = 0                     # keep track of the number of guesses
play = False                    # game flag for main loop and play again feature
guess = -1                      # an impossible starting value, human's guess
win = 0
# Inform the human player about the program - specific to CLI programs
print("Welcome to the guessing game: Hi-Low.")
print("I'm thinking of a number between 1 and 100")
print("You have ten attempts to guess the right number")
print("Would you like to play the game?")
print()
data = input("yes (y/Y) or no (n/N): ")



# Write a while loop as the main game loop
if data == 'y' or data == 'Y':
    print('Alright Lets start shall we!')
    while data == 'y' or data == 'Y':
        guess = input('choose a number from 1,100: ')
        guess = int(guess)
        if guess == number:
                print('wow lucky guess')
                win += 1
                break
        elif guess > number:
                print('WAYY TO HIGH')
                continue
        elif guess < number:
                print('Too low')
                continue
if win >= 1:
    print('you win!!')
    print('--end of program--')
else:
    print('you lose')
    print('--end of program--')

'''  
  # Write the guess and check loop using variables guess and number
    while # your condition here:
    
        # add one to the guess counter
        
        # ask the user for a number between 1 and 100
        
        # check that the string holds a number using a while loop
        
        # if and only if the user has entered a whole number assign guess
        guess = int(data)
        
        # check the guess and report too high or two low
        
        # check number of guesses .. over ten? end the loop
        
    # End of Guess Loop    
    if counter < 10:
        print("Correct! you guessed {0} times.".format(counter))
    elif guess == number:
        print("Max guesses reached, but you guessed right at last")
    else:
        print("Sorry it was {0}. You are out of guesses".format(number))
        
    # Ask to play again - process the play flag according to user input
    
# End of game loop
print("Game Over .. ")
'''