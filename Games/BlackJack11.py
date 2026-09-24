# Title - BlackJack
# Purpose - To create a game of BlackJack for the mid unit assingment
# Author - Victor Daniel Arellana Assia
# Date -  

#Memory - All imports and the creation of the deck and functions 
from colorama import Fore, Back, Style
import random
import time

suits = (Fore.BLACK + '\u2660'+ Fore.BLACK, # Spades
         Fore.BLACK + '\u2663' + Fore.BLACK, # Clubs
         Fore.RED + '\u2665' + Fore.BLACK,  # Hearts
         Fore.RED + '\u2666' + Fore.BLACK) # Diamonds
deck = []
faces = ('A','K','Q','J','T','9','8','7','6','5','4','3','2')

SortCardPlayer = []
PlayerHand = []
HitorStand = False
AmountPlayerCard = 0

SortCardDealer = []
DealerHand = []
AmountDealerCard = 0


game = True
newgame = True



# Setup For Game!

for face in faces:
    for suit in suits:
        deck.append('[' + face + suit + ']')

print(Back.CYAN)
print(Fore.BLACK + "Welcome To BLACKJACK")

# Rules for  new Players
print('\nHere Are The Rules')
time.sleep(2)
print('\nThe aim of the game is to accumulate a higher point total than the dealer, \nbut without going over 21. ')
time.sleep(2)
print('\nThe cards 2 through 10 have their face value,\nT, J, Q, and K are worth 10 points each, and the Ace is worth either 1 or 11 points')
time.sleep(2)
print('\nYou will be going up agaisn\'t a computer,\nyou will start first Good Luck!!')


# Deal Cards
def dealCards(turn):
    '''
    Function That Deals a Card from the deck and removes it so it doesn't appear again
    '''
    card = random.choice(deck) 
    turn.append(card)
    deck.remove(card)
    
# Push Card A To the Back of the counting
def PushA(lst):
    for index in lst:
        if 'A' in lst:
            lst.remove('A')
            lst.append('A')
    return lst

# Total Amount in cards
def total(turn):
    total = 0
    for card in turn:
        if card in ['1','2','3','4','5','6','7','8','9']:
            card = int(card)
            total += card
        elif card in ['J','Q','K','T']:
            total += 10
        else:
            if total > 10:
                total +=1 
            else:
                total +=11
    return total




#Input/Processing 
while game == True:
    if newgame == True:
        newgame = False
        for _ in range (2):
            dealCards(PlayerHand)
            dealCards(DealerHand)
        for sort in range(len(PlayerHand)):
            SortCardPlayer += [PlayerHand[sort][1]]
            SortCardPlayer = PushA(SortCardPlayer)
        for sort in range(len(DealerHand)):
            SortCardDealer += [DealerHand[sort][1]]
            SortCardDealer = PushA(SortCardDealer)
        for index in range (1,len(DealerHand)):  # Code To Print Deck or cards
            print(DealerHand[index-1], end =" ")
            if index % 1 == 0:
                print( '[ ? ]','Dealer Hand')
        for index in range (1,len(PlayerHand) + 1):  # Code To Print Deck or cards
            print(PlayerHand[index-1], end =" ")
            if index % 2 == 0:
                print('Player Hand')
        AmountPlayerCard += 2
        AmountDealerCard += 2
        if total(SortCardPlayer) == 21 or total(SortCardDealer) == 21:
            PlayerTurn = False
            DealerTurn = False
        else:
            time.sleep(2)
            print('\nYou Have', total(SortCardPlayer))
            HitorStand = input('(H)it or (S)tand?: ')
            HitorStand.lower()
            PlayerTurn = True
    if HitorStand == 'h' and PlayerTurn == True:
        dealCards(PlayerHand)
        SortCardPlayer = []
        for sort in range(len(PlayerHand)):
            SortCardPlayer += [PlayerHand[sort][1]]
            SortCardPlayer = PushA(SortCardPlayer)
        HitorStand = 'N'
        AmountPlayerCard += 1
        if total(SortCardPlayer) == 21:
            PlayerTurn = False
            DealerTurn = False
        elif total(SortCardPlayer)>21:
            PlayerTurn = False
            DealerTurn = False
        else:
            for index in range (1,len(DealerHand)):  # Code To Print Deck or cards
                print(DealerHand[index-1], end =" ")
                if index % 1 == 0:
                    print( '[ ? ]','Dealer Hand')
            for index in range (1,len(PlayerHand) + 1):  # Code To Print Deck or cards
                print(PlayerHand[index-1], end =" ")
                if index % len(PlayerHand) == 0:
                    print('Player Hand')
            time.sleep(2)
            print('\nYou Have', total(SortCardPlayer))
            HitorStand = input('(H)it or (S)tand?: ')
            HitorStand.lower()
            PlayerTurn = True
    elif HitorStand == 's' and PlayerTurn == True :
        for index in range (1,len(DealerHand)):  # Code To Print Deck or cards
            print(DealerHand[index-1], end =" ")
            if index % 1 == 0:
                print( '[ ? ]','Dealer Hand')
        for index in range (1,len(PlayerHand) + 1):  # Code To Print Deck or cards
            print(PlayerHand[index-1], end =" ")
            if index % len(PlayerHand) == 0:
                print('Player Hand')
        print('\nYour Final Points', total(SortCardPlayer))
        PlayerTurn = False
        DealerTurn = True
        HitorStand = False
    elif DealerTurn == True:
        if total(SortCardDealer) < 17:
            dealCards(DealerHand)
            AmountDealerCard += 1
            SortCardDealer = []
            for sort in range(len(DealerHand)):
                SortCardDealer += [DealerHand[sort][1]]
                SortCardDealer = PushA(SortCardDealer)
            if total(SortCardDealer) == 21:
                PlayerTurn = False
                DealerTurn = False
            elif total(SortCardDealer)>21:
                PlayerTurn = False
                DealerTurn = False
        elif total(SortCardDealer) > 17 and total(SortCardDealer) < 21:
            DealerTurn = False
    elif DealerTurn == False and PlayerTurn == False:
        if total(SortCardPlayer) == 21:
            for index in range (1,len(DealerHand)+ 1):  # Code To Print Deck or cards
                print(DealerHand[index-1], end =" ")
                if index % AmountDealerCard == 0:
                    print(' Dealer Hand')
            for index in range (1,len(PlayerHand) + 1):  # Code To Print Deck or cards
                print(PlayerHand[index-1], end =" ")
                if index % AmountPlayerCard == 0:
                    print('Player Hand')
            print('\nYou Got ', total(SortCardPlayer), ' BLACKJACK WOOOHOOO')
            print('You Win!')
            break
        elif total(SortCardPlayer) > 21:
            for index in range (1,len(DealerHand)+ 1):  # Code To Print Deck or cards
                print(DealerHand[index-1], end =" ")
                if index % AmountDealerCard == 0:
                    print(' Dealer Hand')
            for index in range (1,len(PlayerHand) + 1):  # Code To Print Deck or cards
                print(PlayerHand[index-1], end =" ")
                if index % AmountPlayerCard == 0:
                    print('Player Hand')
            print('You have', total(SortCardPlayer),'points')
            print('Bust You Lose')
            break
        elif total(SortCardDealer) == 21:
            for index in range (1,len(DealerHand)+ 1):  # Code To Print Deck or cards
                print(DealerHand[index-1], end =" ")
                if index % AmountDealerCard == 0:
                    print(' Dealer Hand')
            for index in range (1,len(PlayerHand) + 1):  # Code To Print Deck or cards
                print(PlayerHand[index-1], end =" ")
                if index % AmountPlayerCard == 0:
                    print('Player Hand')
            print('\nDealer Got ', total(SortCardDealer), ' BLACKJACK WOOOHOOO')
            print('Sorry You Lose')
            break
        elif total(SortCardDealer) > 21:
            for index in range (1,len(DealerHand)+ 1):  # Code To Print Deck or cards
                print(DealerHand[index-1], end =" ")
                if index % AmountDealerCard == 0:
                    print(' Dealer Hand')
            for index in range (1,len(PlayerHand) + 1):  # Code To Print Deck or cards
                print(PlayerHand[index-1], end =" ")
                if index % AmountPlayerCard == 0:
                    print('Player Hand')
            print('Dealer Has', total(SortCardDealer),'points')
            print('Dealer Busts, You Win!!')
            break
        elif total(SortCardPlayer) > total(SortCardDealer):
            for index in range (1,len(DealerHand)+ 1):  # Code To Print Deck or cards
                print(DealerHand[index-1], end =" ")
                if index % AmountDealerCard == 0:
                    print(' Dealer Hand')
            for index in range (1,len(PlayerHand) + 1):  # Code To Print Deck or cards
                print(PlayerHand[index-1], end =" ")
                if index % AmountPlayerCard == 0:
                    print('Player Hand')
            print('\nYou have a total of ', total(SortCardPlayer), ' and the dealer has a total of ', total(SortCardDealer))
            print('You have more points. You Win')
            break
        elif total(SortCardPlayer) < total(SortCardDealer):
            for index in range (1,len(DealerHand)+ 1):  # Code To Print Deck or cards
                print(DealerHand[index-1], end =" ")
                if index % AmountDealerCard == 0:
                    print( 'Dealer Hand')
            for index in range (1,len(PlayerHand) + 1):  # Code To Print Deck or cards
                print(PlayerHand[index-1], end =" ")
                if index % AmountPlayerCard == 0:
                    print('Player Hand')
            print('\nDealer has a total of ', total(SortCardDealer), ' and you have ', total(SortCardPlayer))
            print('The Dealer has more points. You Lose')
            break
        elif total(SortCardPlayer) == total(SortCardDealer):
            print('\nIt\'s a tie!')
            break
    else:
        HitorStand = input('(H)it or (S)tand?: ')
        HitorStand.lower()
