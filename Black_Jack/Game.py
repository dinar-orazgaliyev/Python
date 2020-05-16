import Cards, Bank
import pdb


class Game:

	def __init__(self,name=''):
		self.name = name


	def ready(self):
		entered_answer = input("Are you ready?")
		wanna_replay = False
		if(entered_answer.lower() == 'yes'):
			name = input("What is your name? ")
			self.setName(name)
			Player_Name = self.getName()
			Player_Bank = Bank.Bank(Player_Name, 100)
			Dealer_Bank = Bank.Bank('Dealer', 100)
			#pdb.set_trace()
			self.bets(Player_Bank,Dealer_Bank)
			self.replay(wanna_replay,Player_Bank,Dealer_Bank)

			


		else:
			print("Ok see you next time!")

	def ask_to_replay(self):
		user_input = input("Wanna replay? ")
		if(user_input.lower() == 'yes'):
			return True
		else:
			return False

	def replay(self, wanna_replay,Player_Bank,Dealer_Bank):
			print('\n'*5)
			wanna_replay = self.ask_to_replay()
			while wanna_replay == True and Player_Bank.is_bankrupt() == False and Dealer_Bank.is_bankrupt() == False:
				self.bets(Player_Bank, Dealer_Bank)
				wanna_replay = self.ask_to_replay()

			
			
			if Player_Bank.is_bankrupt() == True:
				print(" Sorry you are bankrupt ")
			elif Dealer_Bank.is_bankrupt() == True:
				print(" Dealer is bankrupt")
			else:
				print(" Ok will play later")
	


	def setName(self,name):
		self.name = name


	def getName(self):
		return self.name

	def gameStarter(self, player_bank, dealer_bank,bet):


		winner = False
		cards_obj = Cards.Cards()
		deck_cards = cards_obj.cards()
		player_cards = cards_obj.random2cards(deck_cards)
		dealer_cards = cards_obj.dealer2cards(deck_cards)
		player_value = cards_obj.cardValueMap(*player_cards)
		dealer_value = cards_obj.cardValueMapDealer(*dealer_cards)
		is_winner = False
		player_hit = []
		dealer_hit = []
		#pdb.set_trace()
		while is_winner == False:
			player_answer = str(input("Type + if you wanna hit?"))
			if player_answer.lower() == '+':
				player_hit.append(cards_obj.hitCard(deck_cards))
				
				player_value = cards_obj.cardValueMap(*player_cards,*player_hit)
				print("You have hit and your hand is {}. Your hit card is {} and the rest cards {}".format(player_value,player_hit,player_cards))
				
				print('\n'*5)
				if player_value > 21:
					print("{} is busted having hand of {}. Dealer has won with hand of {}".format(self.name, player_value, dealer_value))
					dealer_bank.deposit(bet*2)
					print(dealer_bank)
					is_winner = True
				else:
					pass
			else:
				while dealer_value <= 17:
					dealer_hit.append(cards_obj.hitCard(deck_cards))
					print(dealer_hit[-1])
					dealer_value = cards_obj.cardValueMapDealer(*dealer_cards,*dealer_hit)
				if dealer_value > player_value and dealer_value <= 21:
					print("Dealer has won having hand of {}. {}'s' hand is {}".format(dealer_value,self.name,player_value))
					dealer_bank.deposit(bet*2)
					print(player_bank)
					print('\n'*5)
					print(dealer_bank)
					is_winner = True
				elif player_value > dealer_value and player_value <=21:
					print("{} has won having hand of {}. Dealer's hand is {}".format(self.name,player_value,dealer_value))
					player_bank.deposit(bet*2)
					print(player_bank)
					print('\n'*5)
					print(dealer_bank)
					is_winner = True
				elif player_value == dealer_value:
					print("No one has won")
					print(" Dealer cards are {}.".format(dealer_cards))
					player_bank.deposit(bet)
					dealer_bank.deposit(bet)
					print(player_bank)
					print('\n'*5)
					print(dealer_bank)
					break
				else:
					print("Dealer is busted having {}. Hit cards {} and the initial cards {} ".format(dealer_value, dealer_hit, dealer_cards))
					
					player_bank.deposit(bet*2)
					print(player_bank)
					print('\n'*5)
					print(dealer_bank)
					is_winner = True




	
	def bets(self, Player_Bank, Dealer_Bank):
		"""


		RECEIVES OBJECTS OF PLAYER'S BANK AND DEALER'S BANK

		

		"""

		is_sufficient_Player = False
		is_sufficient_Dealer = False
		player_bet = 0
		while is_sufficient_Player == False or is_sufficient_Dealer == False:
			
			try:
				player_bet = int(input("What is your bet? "))
				print('\n'*5)
			
			except:
				print("RANDOM ERROR DO NOT GET IT")
			else:
				is_sufficient_Player = Player_Bank.is_sufficient(player_bet)
				is_sufficient_Dealer = Dealer_Bank.is_sufficient(player_bet)
				if is_sufficient_Player == True and is_sufficient_Dealer == True and player_bet!=0:
					Player_Bank.withdraw(player_bet)
					Dealer_Bank.withdraw(player_bet)
					self.gameStarter(Player_Bank,Dealer_Bank,player_bet)

				elif Player_Bank.is_bankrupt() == True:
					print("You have no money")
					print(Player_Bank)
					print('\n'*5)
					print(Dealer_Bank)
					break
				elif Dealer_Bank.is_bankrupt() == True:
					print("Dealer has no money")
					print(Player_Bank)
					print('\n'*5)
					print(Dealer_Bank)
					break
				else:
					if is_sufficient_Dealer == False:
						print("Please type your bet again. Dealer does not have enough funds ")
					else:
						print("Please type your bet again")
				
		
	









game1 = Game()
game1.ready()



