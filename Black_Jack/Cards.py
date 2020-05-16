"""
Class used for cards used on the deck

"""
import random
import pdb

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
	
	def random2cards(self,deck_cards):
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
			
		
		cards = ((deck_cards[index1_1][index1_2], self.suits[index1_1]), (deck_cards[index2_1][index2_2], self.suits[index2_1] ))
		print("Your cards are {}".format(cards))
		print('\n'*3)
		deck_cards[index1_1][index1_2] = 'Taken'
		deck_cards[index2_1][index2_2] = 'Taken'

		return cards
	
	def dealer2cards(self,deck_cards):
		index1_1 = random.randint(0,3) #suit
		index1_2 = random.randint(0,12) #value

		index2_1 = random.randint(0,3) #suit
		index2_2 = random.randint(0,12) #value
		#print(index1_2, index1_1,  " ", index2_2, index2_1)
		if deck_cards[index1_1][index1_2] == 'Taken':
			while deck_cards[index1_1][index1_2] == 'Taken':
				try:
					index1_1 = random.randint(0,3) #suit
					index1_2 = random.randint(0,12) #value
					card1 = (deck_cards[index1_1][index1_2], self.suits[index1_1]) 
				
				except:
					continue
				else:
				
					deck_cards[index1_1][index1_2] = 'Taken'
				
		else:
			card1 = (deck_cards[index1_1][index1_2], self.suits[index1_1])
			deck_cards[index1_1][index1_2] = 'Taken'

		if deck_cards[index2_1][index2_2] == 'Taken':
			while deck_cards[index2_1][index2_2] == 'Taken':
				try:
					index2_1 = random.randint(0,3) #suit
					index2_2 = random.randint(0,12) #value
					
					card2 = (deck_cards[index2_1][index2_2], self.suits[index2_1]) #, (deck_cards[index2_1][index2_2], self.suits[index2_1] ))
					#print(cards)
					

				except:
					#print("this is error and card is {}".format(card2))
					continue
				else:
					
					deck_cards[index2_1][index2_2] = 'Taken'
					#deck_cards[index2_1][index2_2]
		else:
			card2 = (deck_cards[index2_1][index2_2], self.suits[index2_1])
			deck_cards[index2_1][index2_2] = 'Taken'

		cards = (card1,card2)
		print("First card of the dealer is {}".format(cards[0]))
		print('\n'*3)
		return cards
	
			

	def cardValueMapDealer(self,*args):
		value = 0
		ACE = False
		ACE_index = 0
		for i in range(0,len(args)):
			value = value + self.values[args[i][0]]
			if self.values[args[i][0]] == 11:
				ACE = True
				ACE_index = i


		if value >21 and ACE == True:
			value -= 10


		return value
	def cardValueMap(self,*args):
		value = 0
		ACE = False
		#ACE_index = 0
		for i in range(0,len(args)):
			value = value + self.values[args[i][0]]
			if self.values[args[i][0]] == 11:
				ACE = True


		if ACE == True:
			while ACE == True:
				user_input = int(input("What will be the value for Ace? 1 or 11? "))
				if user_input == 1:
					value -= 10
					print("Ok ACE is 1")
					break
				elif user_input == 11:
					print("Ok ACE is 11 ")
					break
				else:
					print("Please type 1 or 11 ")

		return value

	
	def hitCard(self,deck_cards):
		index1_1 = random.randint(0,3) #suit
		index1_2 = random.randint(0,12) #value

		if deck_cards[index1_1][index1_2] == 'Taken':
			while deck_cards[index1_1][index1_2] == 'Taken':
				try:
					index1_1 = random.randint(0,3) #suit
					index1_2 = random.randint(0,12) #value
					hit_card = (deck_cards[index1_1][index1_2], self.suits[index1_1])
				except:
					continue
				else:
					#print("Your hit card is {}".format(hit_card))
					deck_cards[index1_1][index1_2] = 'Taken'
					break
		else:
			hit_card = (deck_cards[index1_1][index1_2], self.suits[index1_1])
			deck_cards[index1_1][index1_2] = 'Taken'

		return hit_card
	#Here HIT_CARD TO BE ADDED TO PLAYER'S 2 CARDS.


	



if __name__ == "__main__": 
	cards_obj = Cards()
	deck_cards = cards_obj.cards()
	print(deck_cards)
	print('\n'*10)
	cards2 = cards_obj.random2cards(deck_cards)
	print('\n'*5)
	#print(cards2)
	dcards2 = cards_obj.dealer2cards(deck_cards)
	print('\n'*5)
	print("Dealer Cards are {} ".format(dcards2))
	hit_card = cards_obj.hitCard(deck_cards)
	print('\n'*5)
	print(hit_card)
	print('\n'*10)
	print(deck_cards)

	





