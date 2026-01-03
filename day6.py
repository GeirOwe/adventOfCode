# advent of code 
# response to the challenge by geir owe
# day6 - challenge: https://adventofcode.com/2020/day/6

from collections import Counter

#start function
def process_group_input(cForms):
    listToElements = []
    itemsToBeDeleted = []

    #split many responses from one person into single elements. something like:
    for x in range(len(cForms)):
        orgForm = cForms[x]
        for y in range(len(orgForm)):
            listToElements.append(orgForm[y])
        cForms.extend(listToElements)
        listToElements = []
        itemsToBeDeleted.append(orgForm) 
    
    #delete the original entry after adding all the characters
    for x in range(len(itemsToBeDeleted)):
        cForms.remove(itemsToBeDeleted[x])
    
    #count number of unique answers
    newResponse = Counter(cForms).values()
    groupNoOfYes = len(newResponse)
    return groupNoOfYes
#end process_group_input function

#read the test puzzle input
#cform_file = open('day6_test_puzzle_input.txt', 'r')
#read the puzzle input
cform_file = open('day6_puzzle_input.txt', 'r')

#the challenge:
#  For each group, count the number of questions to which 
#  anyone answered "yes". What is the sum of those counts?
noOfYes = 0

#collect all responses from a group
groupInput = []
print()

#loop thru all customs forms and collect responses from each group
for response in cform_file:
    response = response.strip()
    if response == '':
        #all responses from a group is read. Process the forms
        groupNoOfYes = process_group_input(groupInput) 
        noOfYes = noOfYes + groupNoOfYes
        groupInput = []
    else:
        groupInput.append(response)
else:
    #the last customs form
    groupNoOfYes = process_group_input(groupInput) 
    noOfYes = noOfYes + groupNoOfYes
    groupInput = []

print('the number of questions to which anyone answered "yes" ', noOfYes)
print()