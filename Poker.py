'''
File: Poker.py

Description: Simulates a poker game in software
'''
import random
points_hand = []

class Card (object):
	RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

	SUITS = ('C', 'D', 'H', 'S')

	# constructor
	def __init__ (self, rank = 12, suit = 'S'):
		if (rank in Card.RANKS):
			self.rank = rank
		else:
			self.rank = 12

		if (suit in Card.SUITS):
			self.suit = suit
		else:
			self.suit = 'S'

	# string representation of a Card object 
	def __str__ (self):
		if (self.rank == 14):
			rank = 'A'
		elif (self.rank == 13):
			rank = 'K'
		elif (self.rank == 12):
			rank = 'Q'
		elif (self.rank == 11):
			rank = 'J'
		else:
			rank = str (self.rank)
		return rank + self.suit

	# equality tests
	def __eq__ (self, other):
		return self.rank == other.rank

	def __ne__ (self, other):
		return self.rank != other.rank

	def __lt__ (self, other):
		return self.rank < other.rank

	def __le__ (self, other):
		return self.rank <= other.rank

	def __gt__ (self, other):
		return self.rank > other.rank

	def __ge__ (self, other):
		return self.rank >= other.rank

	def value(self):

		prime_list = [2,3,5,7,11,13,17,23,29,31,37,41,43,47]

		return int(prime_list[(self.rank)-1])



class Deck (object):
	# constructor
	def __init__ (self, n = 1):
		self.deck = []
		for i in range (n):
			for suit in Card.SUITS:
				for rank in Card.RANKS:
					card = Card (rank, suit)
					self.deck.append (card)

	# shuffle the deck
	def shuffle (self):
		random.shuffle (self.deck)

	# deal a card
	def deal (self):
		if (len(self.deck) == 0):
			return None
		else:
			return self.deck.pop(0)

class Poker (object):
	def __init__ (self, num_players = 2, num_cards = 5):
		self.deck = Deck()
		self.deck.shuffle()
		self.all_hands = []
		self.numCards_in_Hand = num_cards

		# deal all the hands
		for i in range (num_players):
			hand = []
			for j in range (self.numCards_in_Hand):
				hand.append (self.deck.deal())
			self.all_hands.append (hand)

	# simulates the play of the game
	def play (self):
		# sort the hands of each player and print

		points_hand = []

		for i in range (len(self.all_hands)):
			sorted_hand = sorted (self.all_hands[i], reverse = True)
			self.all_hands[i] = sorted_hand
			hand_str = ''
			for card in sorted_hand:
				hand_str = hand_str + str(card) + ' '
			print ('Player ' + str(i + 1) + ' : ' + hand_str)

		points_hand = []
		points = 0

		#print(game.is_royal(game.all_hands[0]))
		#print(game.is_high_card(game.all_hands[0]))
		order = []
		for i in range(len(self.all_hands)):
			points = 0
			while points == 0:

				points = self.is_royal(self.all_hands[i])
				if points > 0:
					break
				points = self.is_straight_flush(self.all_hands[i])
				if points > 0:
					break
				points = self.is_four_kind(self.all_hands[i])
				if points > 0:
					break
				points = self.is_full_house(self.all_hands[i])
				if points > 0:
					break
				points = self.is_flush(self.all_hands[i])
				if points > 0:
					break
				points = self.is_straight(self.all_hands[i])
				if points > 0:
					break
				points = self.is_three_kind(self.all_hands[i])
				if points > 0:
					break
				points = self.is_two_pair(self.all_hands[i])
				if points > 0:
					break
				points = self.is_one_pair(self.all_hands[i])
				if points > 0:
					break
				points = self.is_high_card(self.all_hands[i])

			points_hand.append(points)
			order.append(i+1)

		hand_name_list = []
		print()
		for i in range(len(self.all_hands)):

				if self.is_royal(self.all_hands[i]):
					hand_name_list.append("Royal Flush")
					continue

				if self.is_straight_flush(self.all_hands[i]):
					hand_name_list.append("Stright Flush")
					continue

				if self.is_four_kind(self.all_hands[i]):
					hand_name_list.append("Four of a Kind")
					continue

				if self.is_full_house(self.all_hands[i]):
					hand_name_list.append("Full House")
					continue

				if self.is_flush(self.all_hands[i]):
					hand_name_list.append("Flush")
					continue

				if self.is_straight(self.all_hands[i]):
					hand_name_list.append("Straight")
					continue

				if self.is_three_kind(self.all_hands[i]):
					hand_name_list.append("Three of a Kind")
					continue

				if self.is_two_pair(self.all_hands[i]):
					hand_name_list.append("Two Pair")
					continue

				if self.is_one_pair(self.all_hands[i]):
					hand_name_list.append("One Pair")
					continue

				if self.is_high_card(self.all_hands[i]):
					hand_name_list.append("High Card")
					continue

		for player in range(len(self.all_hands)):
			print("Player ",end = "")
			print(player+1,end = ": ")
			print(hand_name_list[player])

		print()

		print("Player",end = ": ")
		print((points_hand.index(max(points_hand)))+1 ,"wins.")


		# determine the type of each hand and print
		   # create a list to store points for each hand


		# determine winner and print


	# determine if a hand is a royal flush
	# takes as argument a list of 5 Card objects
	# returns a number (points) for that hand
	def is_royal (self, hand):
		same_suit = True
		for i in range (len(hand) - 1):
			same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

		if (not same_suit):
			return 0

		rank_order = True
		for i in range (len(hand)):
			rank_order = rank_order and (hand[i].rank == 14 - i)

		if (not rank_order):
			return 0
		#10 * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))

		points = (10 ** 10) * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))


		return points

	
	def is_straight_flush (self, hand):
		same_suit = True
		for i in range (len(hand) - 1):
			same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

		if (not same_suit):
			return 0

		rank_order = True
		for i in range (len(hand)-1):
			rank_order = rank_order and (hand[i].rank == hand[i+1].rank + 1)

		if (not rank_order):
			return 0

		points = (10 ** 9) * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))



		return points


		
	def is_four_kind (self, hand):


		points = (10 **8) * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))


		if(hand[0].rank == hand[1].rank) and (hand[1].rank == hand[2].rank) and (hand[2].rank == hand[3].rank):
			return points
		elif (hand[1].rank == hand[2].rank) and (hand[2].rank == hand[3].rank) and (hand[3].rank == hand[4].rank):
			return (10 **8) * (((15 ** 5) + hand[1].rank) + ((15 ** 4) + hand[2].rank) + ((15 ** 3) + hand[3].rank) + ((15 ** 2) + hand[4].rank) +((15) + hand[4].rank))

		return 0

	def is_full_house (self, hand):

		points = (10 ** 7) * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))



		if hand[0].rank == hand[1].rank:
			if hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank:
				return (10 ** 7) * (((15 ** 5) + hand[2].rank) + ((15 ** 4) + hand[3].rank) + ((15 ** 3) + hand[4].rank) + ((15 ** 2) + hand[0].rank) +((15) + hand[1].rank))
			else:
				return 0

		if hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank:
			if hand[3].rank	== hand[4].rank:
				return (10 ** 7) * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))
			else:
				return 0


		return 0



	def is_flush (self, hand):
		
		same_suit = True
		for i in range (len(hand) - 1):
			same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

		if (not same_suit):
			return 0

		points = (10 ** 6) * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))




		return points

		

	def is_straight (self, hand):

		rank_order = True
		for i in range (len(hand)-1):

			rank_order = rank_order and (hand[i].rank == hand[i+1].rank - 1)

		if not rank_order:
			return 0

		points = (10**5) * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))




		return points
		
		
	def is_three_kind (self, hand):
		
		points = (10 ** 4 ) * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))



		if hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank:
			return points 

		if hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank:
			return (10 **4) * (((15 ** 5) + hand[1].rank) + ((15 ** 4) + hand[2].rank) + ((15 ** 3) + hand[3].rank) + ((15 ** 2) + hand[0].rank) +((15) + hand[4].rank)) 

		if hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank:
			return (10 **4) * (((15 ** 5) + hand[2].rank) + ((15 ** 4) + hand[3].rank) + ((15 ** 3) + hand[4].rank) + ((15 ** 2) + hand[0].rank) +((15) + hand[1].rank))

		return 0



	def is_two_pair (self, hand):


		value_list = []

		count = 0

		for i in range(len(hand)-1):
			if (hand[i].rank == hand[i + 1].rank):
				count += 1
				value_list.append(hand[i])
				value_list.append(hand[i+1])

		value_list.sort(reverse = True)

		

		if count == 2:
			for i in range(len(value_list)-1):
				hand.remove(value_list[i])
			points = 100 * (((15 ** 5) + value_list[0].rank) + ((15 ** 4) + value_list[1].rank) + ((15 ** 3) + value_list[2].rank) + ((15 ** 2) + value_list[3].rank) +((15) + hand[0].rank))
			for n in range(len(value_list)-1):
				hand.append(value_list[n])

			hand.sort(reverse = True)

		else:
			return 0

		return points

	# determine if a hand is one pair
	# takes as argument a list of 5 Card objects
	# returns a number (points) for that hand
	def is_one_pair (self, hand):
		one_pair = False
		for i in range (len(hand) - 1):
			if (hand[i].rank == hand[i + 1].rank):
				one_pair = True
				break
		if (not one_pair):
			return 0


		points = 10 * (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))
		return points

	def is_high_card (self, hand):

		points = (((15 ** 5) + hand[0].rank) + ((15 ** 4) + hand[1].rank) + ((15 ** 3) + hand[2].rank) + ((15 ** 2) + hand[3].rank) +((15) + hand[4].rank))

		return points


def main():
	# prompt the user to enter the number of players
	num_players = int (input ('Enter number of players: '))
	while ((num_players < 2) or (num_players > 6)):
		num_players = int (input ('Enter number of players: '))

	print()
	# create the Poker object
	game = Poker (num_players)

	# play the game - poker
	game.play()


# do not remove this line above main()
if __name__ == '__main__':
	main()


		