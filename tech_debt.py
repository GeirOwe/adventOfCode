# A silent movie about technical debt
# by geir owe

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... A short story about technical debt .... >')
    print('  --------------------------------------------')
    print('Presented based on the following from Agile Manifesto')
    print(' "working solution over comprehensive documentation"\n')
    print('so, no powerpoints today!\n')
    print('(note to self: take a pause while the developers are applauding)')
    input()
    print('This fantastic solution will probably blow your mind')
    print('pay attention to the output from the solution')
    print('and not just the delightful code :-)\n')
    input()

def play_the_drums():
    print('.... tromme virvel ....')
    input()
    return

def explain_tech_debt():
    os.system('clear')
    print('< NexUs - Tech debt strategy >')
    print('  --------------------------')
    print('tech debt and financial debt are to be managed in a similar way\n')
    print('equinor financial debt strategy is to ensure financial stability')
    print('equinor tech debt strategy is to ensure business agility\n')
    print('some definitions to link tech debt and financial debt:\n')
    print('custom code & architecture == debt')
    print('refactoring == re-financing\n')
    input()
    return

def explain_nexus_approach():
    os.system('clear')
    print('NexUs approach')
    print('--------------')
    print('replace custom code with standard')
    print('refactor custom code into modern architecture -> clean core\n')
    print('using financial terms: reduce number of loans and re-finance to reduce interest rates')
    input()
    return 

#start function
def process_data(theData):
    expectedResult = 42
    return expectedResult

def get_the_data():
    theData = 80
    return theData

def talk_ended():
    # talk ended, collect reactions
    #
    # reactions = [
    #   participant.applaude()
    #   for participant in audience 
    #   if not participant.sleeping()
    # ]
    return

def start_NexUs():
    #get the data
    theData = get_the_data()
    #process the data and return the answer
    valueX = process_data(theData)
    #technical debt vs financial debt
    explain_tech_debt()
    # what is the nexus strategy on clean core
    explain_nexus_approach()

    print('The technical debt level in SAP ECC is around ', theData, '%')
    print('Equinor financial debt level is to have around 28 %')
    input()
    print('The business expect the tech debt level in NexUs to be -> ')
    play_the_drums()
    print(valueX, '\n')

    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_NexUs()