# advent of code 
# response to the challenge by geir owe
# day6 - challenge: https://adventofcode.com/2020/day/6

from collections import Counter

#start function
def process_group_input(cForms):
    #split many responses from one person into single elements. something like:
    for x in range(len(cForms)):
        if x == 0:                  #answer from first person
            theList = cForms[x]
        else: 
            nextList = cForms[x]    #answer from next person
            # we now use the intersection between the two list 
            # to find common elements among the answers from previous persons and this persons
            theList = list(set(theList).intersection(set(nextList)))
 
    #he number of questions to which anyone answered "yes"
    groupsumOfYes = len(theList)
    return groupsumOfYes
#end process_group_input function

#read the test puzzle input
#cform_file = open('day6_test_puzzle_input.txt', 'r')
#read the puzzle input
cform_file = open('day6_puzzle_input.txt', 'r')

#the challenge:
#  For each group, count the number of questions 
#  to which anyone answered "yes". What is the sum of those counts?
sumOfYes = 0

#collect all responses from a group
groupInput = []
print()

#loop thru all customs forms and collect responses from each group
for response in cform_file:
    response = response.strip()
    if response == '':
        #all responses from a group is read. Process the forms
        groupsumOfYes = process_group_input(groupInput) 
        sumOfYes =  sumOfYes + groupsumOfYes
        #prepare for next group
        groupInput = []
    else:
        groupInput.append(response)
else:
    #the last customs form
    groupsumOfYes = process_group_input(groupInput) 
    sumOfYes =  sumOfYes + groupsumOfYes
    groupInput = []

print('sum of the count of the number of questions to which anyone answered "yes" ',  sumOfYes)
print()