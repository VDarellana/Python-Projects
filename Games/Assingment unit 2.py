# End of UNIT 2: Programming Project - GAME OF PIG
# Purpose - Assignment 2 Computer Science
# Author: Victor Daniel Arellana Assia
# Date: 10/7/2023
#
# Memory 

import random
import time


dice = { 1 : "1",
         2 : "2",
         3 : "3",
         4 : "4",
         5 : "5",
         6 : "6"
         }

die = random.randint(1,6)  # to generate a random die from 1 to 6
play = True                
answer = "N/A"              
humanBank = 0              
humanScore = 0
humanturn = 'true'
computerBank = 100
computerScore = 0
computerturntimes = 0
computerwin ='N/A'


# Welcome Screen 
print("""\
   ___                       __   ___ _      
  / __|__ _ _ __  ___   ___ / _| | _ (_)__ _ 
 | (_ / _` | '  \/ -_) / _ \  _| |  _/ / _` |
  \___\__,_|_|_|_\___| \___/_|   |_| |_\__, |
                                       |___/ """)
# Instructions here
print('These are the rules')
time.sleep(1)
print('The main objective of this game is to reach 100 points first!')
time.sleep(2)
print('You will be playing up agains\'t a computer')
time.sleep(2)
print('You will get turns which you will decide to roll, hold,you will be able to look at your points at the end of your turn')
time.sleep(3)
print('If you roll a 1 your turn will be over and the points rolled in that turn will be lost')
time.sleep(3)
print('If you hold your points in the round will be saved but you will pass your turn')
# Input & Processing - GAME LOOP
while play == True:
    if humanturn == 'true':  
        die = 0
        time.sleep(3)
        answer = input("Do you wish to (r)oll or (h)old?: ")
        die = random.randint(1,6)
        if humanBank >= 100:
            print('you win!!')
            humanturn = 'Win'
        elif answer.lower() == 'r' and die != 1 and humanBank < 100:
            humanScore += die
            time.sleep(1)
            print("you rolled {0}".format(dice.get(die)))
            print("you have", humanScore,"points accumulated this round")
        elif answer.lower() == 'r' and die == 1:
            time.sleep(1)
            print("you rolled {0}".format(dice.get(die)))
            print("You lost your points")
            humanScore = 0
            humanturn = 'lost'
        elif answer.lower() == 'h' and humanScore == 0:
            print('You can\'t save 0 points dummy')
        elif answer.lower() == 'h' and humanBank < 100:
            humanBank += humanScore
            time.sleep(1)
            print('You saved', humanScore,'points its the computers turn now')
            humanScore = 0
            answer = 'NA'
            humanturn = 'lost'
            time.sleep(3)
            print('You have',humanBank,'points and the computer has',computerBank)
        elif humanBank >= 100:
            print('you win!!')
            humanturn = 'Win'
    elif humanturn == 'lost':
        if computerBank >= 100:
            computerwin = 'win'
            humanturn = 'computer won'
            #checks if its almost at 100
        elif computerBank >= 95 and computerBank < 100 and computerturntimes <3 and computerBank + computerScore < 100:
            print('The computer chooses to roll since its about to win')
            die = random.randint(1,6)
            if die == 1:
                time.sleep(2)
                print("The computer rolled {0}".format(dice.get(die)))
                print("The computer lost its points and its turn")
                computerScore = 0
                humanturn = 'true'
                die = 0
                computerturntimes = 0
            elif die != 1:
                print("The computer rolled {0}".format(dice.get(die)))
                computerScore += die
                time.sleep(3)
                print("The computer has", computerScore,"points this round it is deciding its next move...")
                computerturntimes += 1
                #checks if the computer is losing
        elif computerBank <= humanBank and computerBank <= 100 and computerturntimes < 3 and humanBank >= computerScore + computerBank:
            print('The computer chooses to roll since it is losing')
            die = random.randint(1,6)
            time.sleep(3)
            if die == 1:
                print("The computer rolled {0}".format(dice.get(die)))
                time.sleep(3)
                print("The computer lost its points and its turn")
                computerScore = 0
                humanturn = 'true'
                die = 0
                computerturntimes = 0
            elif die != 1:
                print("The computer rolled {0}".format(dice.get(die)))
                computerScore += die
                time.sleep(3)
                print("The computer has", computerScore,"points this round it is deciding its next move...")
                time.sleep(3)
                computerturntimes += 1
        elif computerBank + computerScore >= 100:
            print('The computer has decided to save his points')
            computerBank += computerScore
            humanturn = 'you lost'
            die = 0
            if computerBank >=100:
                humanturn ='you lost'
                computerwin = 'win'
            computerturntimes = 0
            computerScore = 0
            #Checks if the computer is winning
        elif computerBank > humanBank and computerBank<100 and computerturntimes < 1:
            print('The computer has decided to roll')
            if die == 1:
                print("The computer rolled {0}".format(dice.get(die)))
                print("The computer lost its points and its turn")
                computerScore = 0
                humanturn = 'true'
                die = 0
                computerturntimes = 0
            elif die != 1:
                print("The computer rolled {0}".format(dice.get(die)))
                computerScore += die
                if computerBank + computerScore >= 100:
                    computerwin = 'win'
                    print("The computer decided to save and got to 100 points")
                    humanBank = 0
                    humanScore = 0
                    computerBank = 0
                    computerScore = 0
                print("The computer has", computerScore,"points this round it is deciding its next move...")
                time.sleep(3)
                computerturntimes += 1
                #Decides to save
        elif computerBank + computerScore <= 100 :
            print('The computer decided to play it safe')
            computerBank += computerScore
            humanturn = 'true'
            die = 0
            computerturntimes = 0
            computerScore = 0
            
    elif humanturn == 'Win':# Checks if human wins and asks to play again
        print('want to play again?')
        answer = input('Type (y)es or (n)o: ')
        answer.lower()
        if answer == 'y':
            humanturn = 'true'
            humanBank = 0
            humanScore = 0
            computerBank = 0
            computerScore = 0
            computerturntimes = 0
            computerwin = 'NA'
        elif answer == 'n':
            break
    elif computerwin == 'win': # Checks if computer wins and asks to play again
        print("""\
                 ___                   ___              
                / __|__ _ _ __  ___   / _ \__ _____ _ _ 
               | (_ / _` | '  \/ -_) | (_) \ V / -_) '_|
                \___\__,_|_|_|_\___|  \___/ \_/\___|_|  """)
        print('The Computer reached 100 points first')
        print('want to play again?')
        answer = input('Type (y)es or (n)o: ')
        answer.lower()
        if answer =='y':
            humanturn = 'true'
            humanBank = 0
            humanScore = 0
            computerBank = 0
            computerScore = 0
            computerturntimes = 0
            computerwin = 'NA'
        elif answer == 'n':
            break
# Output - End Of Program
print("Thank's for playing!")
print("---End of program---")
