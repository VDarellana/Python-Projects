'''
#Project - Wordle
#Name - Victor Arellana Assia
#Course - Computer Science 1026
#Date - 10/8/2025
#Description - Recreation of the famous game in the pandemic and now wordle with the idea of
projecting the knowledge of functions and loops
'''

#Import of the random words that the user will be able to guess from another file
from randwords import *
#Function that starts the game
def play_game(actual=""):
    # Chooses a random word from the other file and saves it into a variable in the local file if not given one
    if actual != "":
        answer = actual
    else:
        answer = get_rand_word()


    #variables to help with game
    global attempts
    attempts = 1
    print("Word Length:",len(answer)) #lets user know the length of the word
    # Loop that checks the amounts of attempts the user has before losing
    while attempts <= 6:

        guess = guess_word(len(answer))
        if guess == "" :  # Checks that it is a valid input
            print("Incorrect length")
        else:
            win = check_guess(guess, answer)
            print(win)
            if win == ("!" * len(answer)):  # Checks Win and outputs which letters are right
                print("You won !")
                quit()
            elif win != ("!" * len(answer)) and attempts >= 6:
                print(f"You lost, the word was {answer}")
                quit()
            else:
                attempts += 1  # Counts attempts


#Function Checking that the word is only letters and the length of the word that must be guessed
def guess_word(length):
    user_guess = input(f"Guess #{attempts}: ").replace(" ", "")  # Users Guess of the word
    if len(user_guess) == length:
        return user_guess.upper()
    else:
        return ""

#function to compare the users guess to the secret word and see if they have won or print which letters are right or in the wrong spot
def check_guess(guess,actual):
    result = ["^"] * len(guess)
    left_over_actual = list(actual) # list that will check over if there is any letters that match or not and help with the output

    #Pass 1: Right letters
    for letter in range(len(guess)): #Loop purpose to check if any of the letters is right and in the right spot
        if guess[letter] == actual[letter]:
            result[letter] = "!" #Marks that the letter is in the right spot and correct
            left_over_actual[letter] = None #Removes letter from the check list of the guess
    #pass 2: wrong spot
    for letter in range(len(guess)): #Loop purpose to check if any of the letters is right but in the wrong spot
        if guess[letter] in left_over_actual and result[letter] != "!":
            result[letter] = "*" #marks that the letter is in the secret word but not in the correct spot
            left_over_actual[left_over_actual.index(guess[letter])] = None

    return "".join(result) # print statement that will unlock the result of the user list and show the user what they have right

