class Category:
    def __init__(self, p_category): 
        self.ledger = []
        
        self.amount = 0
        self.description = ''
        
        print('class: ' + str(self.ledger)) 
        print('amount: ' + str(self.amount))    
		

    def deposit(self, amount, description):
        self.descriptiom = description
        self.ledger_object = {"amount": self.amount, "description": self.descriptiom}
        self.ledger.append(self.ledger_object)
        self.amount = self.amount + amount         
        
        print('class amount: ' + str(self.amount))
        print('ledger: ' + str(self.ledger))


def create_spend_chart(categories):
    return('100|')


food = Category("Food")
food.deposit(10, "initial deposit")
food.deposit(2, "2nd deposit")