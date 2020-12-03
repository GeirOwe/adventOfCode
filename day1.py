# advent of code by geir owe
# day1

#variables needed
firstExpense = 0
secondExpense = 0
expense_total = 2020 #the sum that the two expenses sum up to
expenses_found = False

#the puzzle input, the expense report
expense_report = [178, 1843, 1841, 6970, 400, 250, 178, 999, 52, 98, 500, 789, 1842]

#some variables to be used while looping
noOfexpenses = len(expense_report)
expenseItem = 0 

#loop over all remaining items in the expense reports
for exp1 in expense_report:
    nextExpense = expenseItem
    
    #loop thru all the remaining expenses, that is listed after this expense
    while nextExpense < (noOfexpenses-1):
        nextExpense = nextExpense + 1
        
        #I'm just expecting one match, if the match is fund we stop
        if expenses_found == False:
            exp2 = expense_report[nextExpense]
            if exp1 + exp2 == expense_total:
                expenses_found = True
                firstExpense = exp1 #store the first expense
                secondExpense = exp2 # store the second expense
                nextExpense = noOfexpenses #stop looking if the match is found
    
    #move to the next expense item in the list
    expenseItem = expenseItem + 1
        
#print results
print('----------------------------------------------------')
print('')
if expenses_found:
    print('first expense: ', firstExpense)
    print('second expense:', secondExpense)
    print('expenses summarized: ', firstExpense + secondExpense)
    print('expenses multiplied:', firstExpense * secondExpense)
else:
    print('check your expenses - some items are missing')

print('number of expenses processed: ', noOfexpenses)
print('')
print('------------------End of print ---------------------')
