"""
Class used for cards used on the deck

"""
import random

class Cards:

	suits = ("Hearts", "Diamonds", "Spades", "Clubs")
	values = {"Two":2, "Three":3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

	def __init__(self):
		"""

		Nothing in here
		
		"""
		pass
	def cards(self):
		value_i = 0
		cards = [[i for i in range(13)] for j in range(4)]

		for i in range(4):
			for value in self.values:

				cards[i][value_i] = value
				value_i += 1
				if value_i == 13:
					value_i = 0
			
		return cards
	def random2cards(self):
		index1_1 = random.randint(0,3) #suit
		index1_2 = random.randint(0,12) #value
		index2_1 = random.randint(0,3) #suit
		index2_2 = random.randint(0,12) #value
		
		while index2_1 == index1_1 and index2_2 == index1_2:
			"""
			This makes sure that 2 cards are not the same
			"""
			index2_1 = random.randint(0,3)
			index2_2 = random.randint(0,12)
			
		deck_cards = self.cards()
		cards = ((deck_cards[index1_1][index1_2], self.suits[index1_1]), (deck_cards[index2_1][index2_2], self.suits[index2_1] ))
	
		return cards
	
	def cardValueMap(self,cards):
		value = self.values[cards[0][0]] + self.values[cards[1][0]]
		print("Your Hand is {}".format(value))

	






cards_obj = Cards()
print(cards_obj.cards())
card3 = cards_obj.random2cards()
#print(card3[0][1])
cards_obj.cardValueMap(card3)




