class Category:
    def __init__(self, p_category): 
        self.ledger = []
        
        self.amount = 0
        self.description = ''
        
        print('class: ' + str(self.ledger)) 
        print('amount: ' + str(self.amount))    
		

    def deposit(self, depositAmount, description=""):
        self.description = description
        self.depositAmount = depositAmount
        ledger_object = {"amount": self.depositAmount, "description": self.description}
        self.ledger.append(ledger_object)
        self.amount = self.amount + self.depositAmount         
        
        print('deposit amount: ' + str(self.amount))
        print('deposit ledger: ' + str(self.ledger))

    def withdraw(self, withdrawAmount, description=""):
        self.withdrawAmount = withdrawAmount
        self.description = description

        if self.withdrawAmount > 0:
            withdrawAmount_neg = self.withdrawAmount * -1
        
        if self.amount + withdrawAmount_neg >= 0:
            print('withdraw amount: ' + str(withdrawAmount_neg))
            self.amount = self.amount + withdrawAmount_neg
            ledger_object = {"amount": withdrawAmount_neg, "description": self.description}
            self.ledger.append(ledger_object)
            
            print('withdraw ledger: ' + str(self.ledger))
            print('new Amount: ' + str(self.amount))
            return True
        else:
            print("No withdraw: " + str(self.withdrawAmount) + ' > ' + str(self.amount))
            return False

    def get_balance(self):
        return self.amount

def create_spend_chart(categories):
    return('100|')


# food = Category("Food")
# food.deposit(10, "initial deposit")
# food.deposit(2, "2nd deposit")
# food.withdraw(3 , "1st withdraw")
# food.withdraw(20, "ineligible withdraw")