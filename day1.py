# advent of code by geir owe
# day1 

#variables needed
firstExpense = 0
secondExpense = 0
thirdExpense = 0

expense_total = 2020 #the sum that the expenses are to sum up to
expenses_found = False

#the puzzle input, the expense report - test
#expense_report = [1721, 979, 366, 299, 675, 1456]

#start function
def get_expenses(expense_file):
    #read a line and loop until all lines are read
    expense_list = []
    for expense in expense_file:
        expenseTrimmed = int(expense.strip())
        expense_list.append(expenseTrimmed)
    return expense_list
#end get_expenses function

#read expenses from the expense file into a list
#expense_report = []
#read the file, the puzzle input
expense_file = open('day1_puzzle_input.txt', 'r')
expense_report = get_expenses(expense_file)

#some variables to be used while looping
#firstExpenseitem contains the position in the expense report for my first number
#secondExpenseitem starts one position after the firstExpenseItem and loops to the end
#thirdExpenseitem starts one position after the secondExpenseItem and loops to the end
noOfexpenses = len(expense_report)
firstExpenseItem = 0 
secondExpenseItem = 0
thirdExpenseItem = 0

#loop over all remaining items in the expense reports
for exp1 in expense_report:
    if expenses_found == False:
        secondExpenseItem = firstExpenseItem
    
    #loop thru all the remaining expenses, that is listed after this expense
    while secondExpenseItem < (noOfexpenses-1):
        #go to the next item in the list looking for second item
        secondExpenseItem = secondExpenseItem + 1
        thirdExpenseItem = secondExpenseItem + 1
        exp2 = expense_report[secondExpenseItem]
        
        while thirdExpenseItem < (noOfexpenses):
            #I'm just expecting one match, if the match is fund we stop
            if expenses_found == False:
                exp3 = expense_report[thirdExpenseItem]
                if exp1 + exp2 + exp3 == expense_total:
                    expenses_found = True
                    firstExpense = exp1 #store the first expense
                    secondExpense = exp2 # store the second expense
                    thirdExpense = exp3 # store the third expense
                    secondExpenseItem = noOfexpenses #stop looking if the match is found
                    thirdExpenseItem = noOfexpenses #stop looking if the match is found
                else:
                    #go to the next item in the list looking for third item
                    thirdExpenseItem = thirdExpenseItem + 1
    
    #move to the next expense item in the list
    firstExpenseItem = firstExpenseItem + 1
        
#print results
print('----------------------------------------------------')
print('')
if expenses_found:
    print('first expense: ', firstExpense)
    print('second expense:', secondExpense)
    print('third expense:', thirdExpense)
    print('expenses summarized: ', firstExpense + secondExpense + thirdExpense)
    print('expenses multiplied:', firstExpense * secondExpense * thirdExpense)
else:
    print('check your expenses - some items are missing')

print('number of expenses processed: ', noOfexpenses)
print('')
print('------------------End of print ---------------------')
