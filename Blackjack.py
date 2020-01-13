'''
File: Blackjack.py

Description: Simulates a game of blackjack
''' 

import  random

class Card (object):
  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

  SUITS = ('S', 'D', 'H', 'C')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if self.rank == 1:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)


class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append(card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)

class Player (object):
  # cards is a list of card objects
  def __init__ (self, cards):
    self.cards = cards

  def hit (self, card):
    self.cards.append(card)

  def getPoints (self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank

    # deduct 10 if Ace is there and needed as 1
    for card in self.cards:
      if count <= 21:
        break
      elif card.rank == 1:
        count = count - 10
    
    return count

  # does the player have 21 points or not
  def hasBlackjack (self):
    return len (self.cards) == 2 and self.getPoints() == 21

  # complete the code so that the cards and points are printed
  def __str__ (self):
    for n in range (len(self.cards)):
      return (' '.join(map(str,self.cards))) + " - " + str(self.getPoints()) + " points"

# Dealer class inherits from the Player class
class Dealer (Player):
  def __init__ (self, cards):
    Player.__init__ (self, cards)
    self.show_one_card = True

  # over-ride the hit() function in the parent class
  # add cards while points < 17, then allow all to be shown
  def hit (self, deck):
    self.show_one_card = False
    while self.getPoints() < 17:
      self.cards.append (deck.deal())

  # return just one card if not hit yet by over-riding the str function
  def __str__ (self):
    if self.show_one_card:
      return str(self.cards[0])
    else:
      return Player.__str__(self)

class Blackjack (object):
  def __init__ (self, numPlayers = 1):
    self.deck = Deck()
    self.deck.shuffle()

    self.numPlayers = numPlayers
    self.Players = []

    # create the number of players specified
    # each player gets two cards
    for i in range (self.numPlayers):
      self.Players.append (Player([self.deck.deal(), self.deck.deal()]))

    # create the dealer
    # dealer gets two cards
    self.dealer = Dealer ([self.deck.deal(), self.deck.deal()])

  def play (self):
    # Print the cards that each player has
    for i in range (self.numPlayers):
      print ('Player ' + str(i + 1) + ': ' + str(self.Players[i]))

    # Print the cards that the dealer has
    print ('Dealer: ' + str(self.dealer))

    # Each player hits until he says no
    playerPoints = []
    bustPoints = []
    BlackList = []
    for i in range (self.numPlayers):
      while True:
        print("Player",(str(i+1)),end=": ")
        choice = input ('do you want to hit? [y / n]: ')
        if choice in ('y', 'Y'):
          (self.Players[i]).hit (self.deck.deal())
          points = (self.Players[i]).getPoints()
          Black = (self.Players[i]).hasBlackjack()
          BlackList.append(Black)
          print ('Player ' + str(i + 1) + ': ' + str(self.Players[i]))
          if points >= 21:
            print()
            break
        else:
          print()
          break
      playerPoints.append ((self.Players[i]).getPoints()%22)
      bustPoints.append ((self.Players[i]).getPoints())

    # Dealer's turn to hit
    self.dealer.hit (self.deck)
    dealerPoints = [self.dealer.getPoints()]
    print ('Dealer: ' + str(self.dealer))
    dealerBlack = self.dealer.hasBlackjack()

    # determine the outcome; you will have to re-write the code
    # it was written for just one player having playerPoints
    # do not output result for dealer
    lose = False
    print()
    #print(playerPoints)
    if max(dealerPoints) > 21:
      print ('Dealer loses')
      print()
      for i in range(self.numPlayers):
        if bustPoints[i] <= 21:
          print("Player",i+1,"wins")
      print()
      for i in range(self.numPlayers):
        if bustPoints[i] > 21:
          print("Player",i+1,"loses")        
    elif max(dealerPoints)%22 > max(playerPoints)%22 or (min(playerPoints)) > 21:
      print ('Dealer wins')
    elif (max(dealerPoints)%22 < max(playerPoints)%22 and max(playerPoints) <= 21):
      #print ('Player',(playerPoints.index(max(playerPoints))+1), 'wins')
      winner = (max(playerPoints))%22
      lose = True
    elif max(dealerPoints)%22 == max(playerPoints)%22:
      for check in BlackList:
        if check == True:
          print("Player",BlackList.index(check)+1,"wins")
        else:
          pass
      if dealerBlack:
        print ('Dealer wins')
        #print("passed dealerBlack")
      else:
        print ('There is a tie')
    print()
    #print(playerPoints)
    if lose:
      for i in range(self.numPlayers):
        if playerPoints[i] == winner or (playerPoints[i] < 21 and playerPoints[i] > max(dealerPoints)):
          print("Player",i+1,"wins")
      print()
      for i in range(self.numPlayers):
        if playerPoints[i] != winner and not (playerPoints[i] < 21 and playerPoints[i] > max(dealerPoints)):
          print("Player",i+1,"loses")      

def main ():
  numPlayers = eval (input ('Enter number of players: '))
  while (numPlayers < 1 or numPlayers > 6):
    numPlayers = eval (input ('Enter number of players: '))
  game = Blackjack (numPlayers)
  game.play()

if __name__ == '__main__':
  main()
