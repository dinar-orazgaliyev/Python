"""
Class used for balance manipulations
"""
class Bank:
    
    def __init__(self,owner,balance):
        """
        Constructor for bank. For player's funds, dealer's funds and bank on the deck.

        """
        self.owner = owner
        self.balance = balance
        #print(f"Account owner: {self.owner} \nAccount Balance: {self.balance}")
        print("{}'s balance is {}".format(self.owner,self.balance))
    def deposit(self, deposit_money):
        """
        For bank on the Deck, player cannot bet more money than dealer has.
        This method is invoked once dealer or player has won.  Bank goes to balance of player or dealer.
        """
        self.balance += deposit_money
       
    def withdraw(self,withdrawal_money):
        """
        This method is used for bets
        """
        if self.balance < withdrawal_money:
            print("Funds are insufficient")
            
        else:
            self.balance -= withdrawal_money
            print("Withdrawal Accepted")

    def is_sufficient(self,withdrawal_money):
        if self.balance < withdrawal_money:
            return False
        else:   
            return True
    def is_bankrupt(self):
        if self.balance == 0:
            return True
        else:
            return False
    def __str__(self):
        return f"Account owner: {self.owner} \nMoney: {self.balance}"
    