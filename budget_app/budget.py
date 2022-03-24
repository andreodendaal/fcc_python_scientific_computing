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
    #category_str = categories[0]
    withdraw_total = 0
    withdraw_category = []
    withdraw_amounts = []
    #process category objects
    for i, value in enumerate(categories):
        withdraw_category.append(value.category)
        withdraw_amounts.append(value.withdrawAmount)

    withdraw_total = sum(withdraw_amounts)
    withdraw_percent = []

    for i, value in enumerate(withdraw_amounts):
        percentage = (100*value)/withdraw_total
        withdraw_percent.append(percentage)

    #matrix_width = len(categories) + 3
    matrix_width = len(categories) + 3
    matrix_depth = 11 
    matrix = [['   ' for x in range(matrix_depth)] for x in range(matrix_width)]
    
    #print(matrix)
    matrix[0][0] = '100'
    matrix[0][1] = ' 90'
    matrix[0][2] = ' 80'
    matrix[0][3] = ' 70'
    matrix[0][4] = ' 60'
    matrix[0][5] = ' 50'
    matrix[0][6] = ' 40'
    matrix[0][7] = ' 30'
    matrix[0][8] = ' 20'
    matrix[0][9] =  ' 10'
    matrix[0][10] = '  0'

    matrix[1][0] = '| '
    matrix[1][1] = '| '
    matrix[1][2] = '| '
    matrix[1][3] = '| '
    matrix[1][4] = '| '
    matrix[1][5] = '| '
    matrix[1][6] = '| '
    matrix[1][7] = '| '
    matrix[1][8] = '| '
    matrix[1][9] = '| '
    matrix[1][10] = '| '
    
    
    for i, value in enumerate(matrix[matrix_width-1]):
        matrix[matrix_width-1][i] = '\n'

    #print(matrix)

    # Process %'ages
    for i, value1 in enumerate(withdraw_percent):
        for x in range(matrix_depth):            
            percent_test = int((matrix[0][x]))
            if value1 >= percent_test:
                matrix[i+2][x] = 'o'

    #print(matrix)

    top_line =  "Percentage spent by category\n"
    sum_line = '    ----------\n'
    return_string =  top_line 

    #for x in range(matrix_depth):
    x=0
    for x in range(matrix_depth):    
        line = ''
        for y in range(matrix_width):
            value = matrix[y][x] 
            if value == 'o':               
                value = 'o  '
            elif value == ' ':
                value = value 

            line = line + value     
        return_string = return_string + line
        #print(return_string)
    
    return_string = return_string + sum_line
  
    # X axis lable matrix
    
    label_matrix_width = len(categories) + 2
    
    label_depth = len(max(withdraw_category, key=len))
    label_matrix = [['' for x in range(label_depth)] for x in range(label_matrix_width)]

    for i, category_str in enumerate(withdraw_category):
        for x, str_element in enumerate(category_str):                    
                label_matrix[i+1][x] = str_element

    for i, value in enumerate(label_matrix[label_matrix_width-1]):
        #dont do the very last element
        if i < label_depth - 1:
            label_matrix[label_matrix_width-1][i] = '\n'
        else:
            label_matrix[label_matrix_width-1][i] = ''

    #print(label_matrix)

    #process X Lable
    x=0
    for x in range(label_depth):
        line = ''
        for y in range(label_matrix_width):
            value = label_matrix[y][x] 
            if value == '':
                 value = ' ' 
            else:
                 value = value 
 
            if (y == (label_matrix_width -1)) and (x == (label_depth -1)):
                line = line + '  '               
            else:                
                line = line + '  ' + value 

        return_string = return_string + line
        #print(return_string)

    #print(return_string)
    

    return(return_string)



# food = Category("Food")
# entertainment = Category("Entertainment")
# business = Category("Business")
# whatever = Category("whatever")
# whatever.deposit(1, "deposit")
# whatever.withdraw(1.00)
# food.deposit(900, "deposit")
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)

# actual = create_spend_chart([business, food, entertainment, whatever])
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