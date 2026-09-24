'''
#Project - Wordle
#Name - Victor Arellana Assia
#Date - 10/8/2025
#Description - Recreation of the famous game in the pandemic and now wordle with the idea of
projecting the knowledge of functions and loops
'''

#Import of the random words that the user will be able to guess from another file
from randwords import *
#Function Checking that the word is only letters and the length of the word that must be guessed
def guess_word(length):
    if len(length) == len(answer) and length.isalpha() == True :
        return True
    else:
        print("invalid answer")
        return False
#function to compare the users guess to the secret word and see if they have won or print which letters are right or in the wrong spot
def check_guess(guess,actual):
    result = ["^"] * len(guess)
    leftOverActual = list(actual) # list that will check over if there is any letters that match or not and help with the output

    for letter in range(len(guess)): #Loop purpose to check if any of the letters is right and in the right spot
        if guess[letter] == actual[letter]:
            result[letter] = "!" #Marks that the letter is in the right spot and correct
            leftOverActual[letter] = None #Removes letter from the check list of the guess
    for letter in range(len(guess)): #Loop purpose to check if any of the letters is right but in the wrong spot
        if guess[letter] in actual and guess[letter] in leftOverActual :
            result[letter] = "*" #marks that the letter is in the secret word but not in the correct spot
            leftOverActual[leftOverActual.index(guess[letter])] = None
    print(*result, sep="")# print statement that will unlock the result of the user list and show the user what they have right
    if result == (["!"] * len(guess)):#Win statement that checks if result is all Green/corrects
        return True
    else:
        return False

#Function that starts the game
def play_game():
    word = get_rand_word() #Chooses a random word from the other file and saves it into a variable in the local file
    print("Word Length:",len(word)) #lets user know the length of the word

    return word

#Local variables to help with game
userGuess = ""
attempts = 1
answer = play_game()
win = False
#Loop that checks the amounts of attempts the user has before losing
while attempts <= 6 :
     userGuess= input(f"Guess #{attempts}: ").upper().replace(" ", "")#Users Guess of the word
     if guess_word(userGuess) == True:#Checks that it is a valid input
        win = check_guess(userGuess,answer)
        if check_guess(userGuess, answer) == True:#Checks Win and outputs which letters are right
            print("You won!")
            quit()
        else:
             attempts +=1 #Counts attempts

print(f"You lost. the word was {answer}")