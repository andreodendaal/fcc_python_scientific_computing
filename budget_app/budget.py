class Category:
    def __init__(self, category): 
        self.ledger = []
        
        self.amount = 0
        self.category = category
        #print_output = str(self)
        #return print_output     
        #print('class: ' + str(self.ledger)) 
        #print('amount: ' + str(self.amount))   
        # 
    # def __repr__(self):
    #     return_string =  "*************% s*************" % (self.category) + "/n"
    #     #return_string =  "*************% s*************:% s " % (self.category , self.ledger)
    #     self.total = 0
    #     for key in self.ledger:
    #         # for item in key:
    #         #     return_string =  return_string + str(key[item])
    #         return_substring23 = "{:<23}".format(key["description"][:23])
    #         return_number = "{:.2f}".format(key["amount"])
    #         self.total = self.total + key["amount"]
    #         return_substring07 = "{:>7}".format(str(return_number))

    #         return_string = return_string + return_substring23 + return_substring07 + "/n"

    #     return_total = "{:.2f}".format(self.total)
    #     return_string = return_string + "Total:" + "{:>7}".format(str(return_total))

        # return return_string

    def __str__(self):
        return_string =  "*************% s*************" % (self.category) + "\n"
        
        self.total = 0
        for key in self.ledger:         
            return_substring23 = "{:<23}".format(key["description"][:23])
            return_number = "{:.2f}".format(key["amount"])
            self.total = self.total + key["amount"]
            return_substring07 = "{:>7}".format(str(return_number))

            return_string = return_string + return_substring23 + return_substring07 + "\n"

        return_total = "{:.2f}".format(self.total)
        return_string = return_string + "Total:" + "{:>7}".format(str(return_total))

        return return_string 
            
	 

    def deposit(self, depositAmount, description=""):
        self.description = description
        self.depositAmount = depositAmount
        ledger_object = {"amount": self.depositAmount, "description": self.description}
        self.ledger.append(ledger_object)
        self.amount = self.amount + self.depositAmount         
        
        #print('deposit amount: ' + str(self.amount))
        #print('deposit ledger: ' + str(self.ledger))

    def withdraw(self, withdrawAmount, description=""):
        self.withdrawAmount = withdrawAmount
        self.description = description

        if self.withdrawAmount > 0:
            withdrawAmount_neg = self.withdrawAmount * -1
        
        if self.amount + withdrawAmount_neg >= 0:
            #print('withdraw amount: ' + str(withdrawAmount_neg))
            self.amount = self.amount + withdrawAmount_neg
            ledger_object = {"amount": withdrawAmount_neg, "description": self.description}
            self.ledger.append(ledger_object)
            
            #print('withdraw ledger: ' + str(self.ledger))
            #print('new Amount: ' + str(self.amount))
            return True
        else:
            #print("No withdraw: " + str(self.withdrawAmount) + ' > ' + str(self.amount))
            return False

    def get_balance(self):
        return self.amount

    def transfer(self, amount, category):
        self.withdrawal_amount = amount
        self.destination_category = category.category
        if self.check_funds(self.withdrawal_amount):
            self.description = "Transfer to " + str(self.destination_category)
            ledger_object = {"amount": (self.withdrawal_amount * -1), "description": self.description}
            self.ledger.append(ledger_object)
            self.amount = self.amount - self.withdrawal_amount

            category.amount = category.amount + self.withdrawal_amount
            self.description = "Transfer from " + str(self.category)
            transfer_ledger_object = {"amount": self.withdrawal_amount, "description": self.description}
            category.ledger.append(transfer_ledger_object)
            return True
        else:
            return False

    def check_funds(self, amount):
        self.check_amount = amount * -1
        if self.amount + self.check_amount >= 0:
            return True
        else:
            return False
    




def create_spend_chart(p_categories):
    categories = p_categories
    category_str = categories[0]
    print(categories[0].category)
    print(categories[1])
    print(categories[2])
    matrix = [['100'], ['90', '0'], ['80', '0', '0']]
    matrix = [[0 for x in range(10)] for x in range(len(categories))]
    print(matrix)
    return_string =  "Percentage spent by category" + "\n"


    return(return_string)

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

actual = create_spend_chart([business, food, entertainment])
#print(actual)

# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)
# print(str(food))
# food = Category("Food")
# food.deposit(10, "initial deposit")
# food.deposit(2, "2nd deposit")
# food.withdraw(3 , "1st withdraw")
# food.withdraw(20, "ineligible withdraw")