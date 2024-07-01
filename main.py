import random
from art import logo
from replit import clear
############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11 or 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#break it down
#1 Create a function in which you give your cards, pickupcard#. It outputs new hand. calculate hand with special case of ace



def hitme(cardsScore, cards, pickupnumber):
  '''Adds new cards to your current hand of cards. yourhand is the score. yourhand rows is the print  '''
  #create a deck of cards (1-10,Jack/Queen/King all count as 10)
  deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  facecards = ['J', 'Q', 'K', 10]
  #Randomly choose x cards from the deck add to your hand of cards
  for i in range(pickupnumber):
    cardsScore.append(random.choice(deck))
    # Adding facecards to cards if last element in cardScore is 10 
    if cardsScore[-1] == 10:
      cards.append(random.choice(facecards))
    else:
      #Take the last element from the list
      cards.append(cardsScore[-1])
  return cardsScore, cards

def calcAceScore(cardsScore):
  '''Calculates and adjusts for ace scores'''
  #Find the ace (1) indices 
  aceIndices =[k for k, value in enumerate(cardsScore) if value == 1]
  # Calculate the total score with an ace (1 or 11)
  for index in aceIndices:
    if cardsScore[index] ==1:
      cardsScore[index] = 11
      if sum(cardsScore) > 21:
        cardsScore[index] = 1
  return cardsScore
  

def generateSuits(rowsuits, numberofcards):
  """Generates the Suites for the cards"""
  suits = ['♥','♦','♠','♣']
  for i in range(numberofcards):
    rowsuits.append(random.choice(suits))
  return rowsuits

    

def displayCards(cards, cardsSuit):
  """Display all the cards in the cards list. """
  # The text to display on each row.
  rows = ['', '', '', '', '']

  for i in range(len(cards)):

      rows[0] += ' ___  '  # Print the top line of the card.
      # Print the card's front
    
      if cards[i] == 'BACKSIDE':
          rows[1] += '|## | '
          rows[2] += '|###| '
          rows[3] += '|_##| '
      elif cards[i] == 10 :
          rows[1] += '|{} | '.format(cards[i])
          rows[2] += '| {} | '.format(cardsSuit[i])
          rows[3] += '|_{}| '.format(cards[i])
      elif cards[i] == 'K' or cards[i] == 'J' or cards[i] == 'Q':
          rows[1] += '|{}  | '.format(cards[i])
          rows[2] += '| {} | '.format(cardsSuit[i])
          rows[3] += '|__{}| '.format(cards[i])
      elif 1 < cards[i] < 10 :
          rows[1] += '|{}  | '.format(cards[i])
          rows[2] += '| {} | '.format(cardsSuit[i])
          rows[3] += '|__{}| '.format(cards[i])
      elif (cards[i] == 1) | (cards[i] ==11):
          rows[1] += '|A  | '
          rows[2] += '| {} | '.format(cardsSuit[i])
          rows[3] += '|__A| '

# Print each row on the screen:
  for row in rows:
      print(row)




#set program is running status to True, empty hands for user and dealer
isProgramRunning = True
print(logo)

while(isProgramRunning):
  # Ask the user if they are playing blackjack
 
  isPlayingBlackjack = ('y' == input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
  if isPlayingBlackjack:
    #initialize the game
    clear()
    yourCards = []
    yourCardsScore = []
    yourCardsSuit = []
    dealerCards = []
    dealerCardsScore = []
    dealerCardsSuit =[]
    result =""

    #Randomly choose 2 choose cards for yourCards and dealerCards
    yourCardsScore, yourCards = hitme(yourCardsScore,yourCards,2)
    yourCardsScore = calcAceScore(yourCardsScore) 
    yourCardsSuit = generateSuits(yourCardsSuit,2)
    
      
    dealerCardsScore, dealerCards = hitme(dealerCardsScore,dealerCards,2)
    dealerCardsScore = calcAceScore(dealerCardsScore)
    dealerCardsSuit = generateSuits(dealerCardsSuit,2)
    
    #No black jack has occured for user
    if not (sum(yourCardsScore) == 21):
        
      while sum(yourCardsScore) < 21:
        clear()
        print(logo)
        print("DEALER'S HAND:")
        print(f"(Total: {dealerCardsScore[1]})")
        displayCards(['BACKSIDE'] + dealerCards[1:],dealerCardsSuit)
        print("YOUR HAND:")
        print(f"(Total: {sum(yourCardsScore)})")
        displayCards(yourCards,yourCardsSuit)
        
      
        
  
        
        #Ask would like another card?
        isAddingCard = input("Type 'y' to get another card, type 'n' to pass: ") == 'y'
        if isAddingCard:
          yourCardsScore, yourCards = hitme(yourCardsScore,yourCards,1)
          yourCardsScore = calcAceScore(yourCardsScore)
          yourCardsSuit = generateSuits(yourCardsSuit,1)
            
        else:
          break
  
      #Calculate the dealers cards
      while sum(dealerCardsScore) < 17:
        #add a card to dealers hand
        dealerCardsScore, dealerCards = hitme(dealerCardsScore,dealerCards,1)
        dealerCardsScore = calcAceScore(dealerCardsScore)
        dealerCardsSuit = generateSuits(dealerCardsSuit,1)
      
      #all possible cases
      if sum(yourCardsScore) > 21:
        result = "You went over, you lose 😭"
      elif sum(dealerCardsScore) > 21:
        result = "Dealer went over, you win 🥇"
      elif sum(dealerCardsScore) == sum(yourCardsScore):
        result = "Draw"
      elif sum(dealerCardsScore) < sum(yourCardsScore):
        result = "You win! 🥇"
      elif sum(dealerCardsScore) > sum(yourCardsScore):
        result = "You lose 😭"
        
     
      #user black jack has occured
    else:
      #Calculate dealer cards
      while sum(dealerCardsScore) < 17:
        #add a card to dealers hand
        dealerCardsScore, dealerCards = hitme(dealerCardsScore,dealerCards,1)
      if sum(yourCardsScore) == sum(dealerCardsScore):
        result = "Draw"
      elif sum(yourCardsScore) > sum(dealerCardsScore):
        result = "You win! black jack 🥇 "
      
  
    clear()
    print(logo)
    print("DEALER'S HAND:")
    print(f"(Total: {sum(dealerCardsScore)})")

    displayCards(dealerCards,dealerCardsSuit)
    print("YOUR HAND:")
    print(f"(Total: {sum(yourCardsScore)})")
  
    displayCards(yourCards,yourCardsSuit)
    print(result)
  
  #Else user is not playing blackjack 
  else:
    #end program
    isProgramRunning = False

   

###########################################
    
#create a deck of cards (1-10,Jack/Queen/King all count as 10)
#set program is running status to True

# While program is running
  # Ask the user if they are playing blackjack
  # if user is playing blackjack

    #Randomly choose 2 choose cards for yourCards and dealerCards
    #Display Blackjack logo
    #Display your cards, your current score, one of dealer cards

    #while your current score < 21

      #Ask the user if they would like another card?

      #If user takes another card
        #Calculate and Display your cards, your current score, one of dealer cards
        #If your current score > 21
          #Display your cards, your current score, one of dealer cards
          #Display You went over. You lose
      #endif

      #Else if user doesn't take another card
        # while dealers score < 17
          #add a card to dealers hand , calculate dealers scorescore
        #end while

        #Calculate your current score, dealers score 

        #if dealers score == your score
            #display "Draw"

        #if dealers score < your score
            # display you win
        #if dealers score > your score
            # display you lose
      #endelse

  #Else if user is not playing blackjack 
    #set program is running to False
