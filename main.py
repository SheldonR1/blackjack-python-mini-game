###############  Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#Global Variables
from art import logo;
import random
import os #used to clear screen
cards = [ 'A',2,3,4,5,6,7,8,9,10,'J','Q','K']
playerStack=[]
dealerStack=[]
runState=True;
playerCardValue=0
dealerCardValue=0

def endGame():
  userInput=input("Do you want to play again Y/N?").upper()
  if userInput=='Y':
   global playerStack
   global dealerStack
   playerStack=[]
   dealerStack=[]  
  else:
   global runState
   runState=False

#generate random card
def getNewCard():
  return random.choice(cards)


#function to get startup cards
def getStartCards():
  
  #add cards to stack
  playerStack.append(getNewCard())
  playerStack.append(getNewCard())
  dealerStack.append(getNewCard())
  dealerStack.append(getNewCard())
  print(f" \n The dealer's cards are: {dealerStack[0]} and ?")
  print(f" \n Your cards are: {playerStack[0]} and {playerStack[1]} \n =================================================================== ")
  
def returnCardValue(val):
  valStr=val
  if valStr=='A':
    return 1
  elif ((valStr=="J") | (valStr=="Q") | (valStr=="K")):
    return 10
  else:
    return valStr
    
def whoWins(playerVal, dealerVal):
  print(" ++++++++++++++++ THE RESULTS YOU'VE BEEN WAITING FOR +++++++++++++")
  #CHECK IF ANYONE IS BUST
  if playerVal > 21:
    print(f"YOU LOST... You had {playerVal} against {dealerVal}")
    if dealerVal > 21:
      print("THE DEALER ALSO LOST")
  elif (playerVal < dealerVal) & (dealerVal < 22):
    print(f"The Dealer WON... You had {playerVal} against {dealerVal}")
  elif playerVal > dealerVal & (playerVal < 22):
    print(f"YOU WIN... You had {playerVal} against {dealerVal}")
  elif playerVal == dealerVal:
    print(f"ITS A TIE... You had {playerVal} against {dealerVal}")
    if playerVal > 21 & dealerVal > 21:
      print("BUT YOU BOTH LOST")
    print("===================================================================")  
  endGame()  
 
def checkDealerCards():
  #determine current dealerCardValue
  dealerCardValue=0
  shouldDealerAddCard=False
  shouldDealerAddCardAgain=False
  print(f"------------------------------YOUR CARDS: -----------------------")
  print(playerStack, sep='\n')
  print(f" --------------------------The Dealers Cards: --------------------")
  print(dealerStack, sep='\n')
  if ((returnCardValue(dealerStack[0])==1) & (returnCardValue(dealerStack[1])==10)) | ((returnCardValue(dealerStack[0])==10) & (returnCardValue(dealerStack[1])==1)):
       print("THE DEALER GOT BLACKJACK 🃏")
       dealerCardValue=21
  else:
    for item in dealerStack:
      dealerCardValue+=returnCardValue(item)
    if(dealerCardValue <= 10): 
     shouldDealerAddCard=True
    if shouldDealerAddCard==True:
      dealerStack.append(getNewCard())
      print ("Dealer is adding a card")
      newValue=returnCardValue(dealerStack[-1])
      dealerCardValue=dealerCardValue + int(newValue)
      print (f"New DealerHand: {dealerStack}")          
    if dealerCardValue < 14:
     shouldDealerAddCardAgain=random.choice([True, False])
    if shouldDealerAddCardAgain==True:
      dealerStack.append(getNewCard())
      print ("Dealer is adding a card")
      newValue=returnCardValue(dealerStack[-1])
      dealerCardValue=dealerCardValue + int(newValue)
      print (f"New DealerHand: {dealerStack}")
    
  return dealerCardValue
    #randomly choose to add a card?
         

def addCard():
   userInput = str(input("Do you want to add a card? Y/N:")).upper()
   if userInput=='Y':
      playerStack.append(getNewCard())
      print(f"\n     Your newCard is {playerStack[-1]}")
      checkPlayerCards()
   elif userInput=='N':
     return 
   else:
     addCard() #FORCE THEM TO INPUT A CORRECT VALUE


def checkPlayerCards():
  #check for immediate blackjack
  global playerCardValue
  playerCardValue=0 #this part wouldnt be necessary if it wasnt for the loop
  #  #check player's current score #I KNOW THIS IS PROCESSOR HEAVY/AN UNECESSARY LOOP THAT OCULD BE REPLACED BY AN INT TO TRACK THE NUM CARDS IN PLAYER HAND TO ADD THAT TO TOTAL BUT I WANTED TO DO A LOOP ANYWAYS TO PROVE I REMEMBER HOW TO DO THEM
  for item in playerStack:
   output1=returnCardValue(item)
   playerCardValue+=int(output1)

  if playerCardValue < 21:
    addCard()
  elif playerCardValue > 21:
    print(f"\n You went bust a total of {playerCardValue}")
  elif playerCardValue == 21:
    print(f" \nYou're on the money at {playerCardValue} lets see what the dealer has")
  else:
    print(f"ERROR YOU SHOULD SEE THIS SOMETHING WENT WRONG WITH checkingPlayerCards() and playerCardValue= {playerCardValue}")
    endGame()
  return playerCardValue
    

############### MAIN ##############################
while runState:
  os.system('clear') 
  print(logo)
  getStartCards() 
  playerSum=int(checkPlayerCards()) 
  dealerSum=int(checkDealerCards())
  whoWins(playerSum,dealerSum)
