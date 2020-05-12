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
        print("Your balance is {}".format(self.balance))
    def deposit(self, deposit_money):
        """
        For bank on the Deck, player cannot bet more money than dealer has.
        This method is invoked once dealer or player has won.  Bank goes to balance of player or dealer.
        """
        self.balance += deposit_money
        print("Now ")
    def withdraw(self,withdrawal_money):
        """
        This method is used for bets
        """
        if self.balance < withdrawal_money:
            print("Funds are insufficient")
        else:
            self.balance -= withdrawal_money
            print("Withdrawal Accepted")
    def __str__(self):
        return f"Account owner: {self.owner} \nMoney: {self.balance}"