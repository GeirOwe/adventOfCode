# day 4 advent of code 2020
# by GeirOwe
# the challenge: https://adventofcode.com/2020/day/4

import pandas as pd 

#process the input file and return a dataframe with all passports
def process_passports(pass_file):
    #process input - move them into a dictionary to make it possible to process
    onePassport = {}
    listofPassports = []
    for onePass in pass_file:
        onePass = onePass.strip()
        if onePass == '':
            listofPassports.append(onePassport)
            onePassport = {}
        else:
            # Converting string from the input file into dictionary - this is easier to process
            Dict = dict((x.strip(), y.strip()) 
                for x, y in (element.split(':')  
                for element in onePass.split(' ')))
            onePassport.update(Dict)
    # add the last row also - for some reason not included in loop
    listofPassports.append(onePassport)
    return listofPassports 
#end of process_passports function

#find passports with errors - i.e. missing information
def check_pass_for_err(df):
    # any passport where these columns is missing info, null / NaN, are invalid
    errPass = df[df['ecl'].isnull() | df['pid'].isnull() | df['eyr'].isnull() | df['hcl'].isnull() | df['byr'].isnull() | df['iyr'].isnull() | df['hgt'].isnull()]
    invalidPassports = len(errPass)
    return invalidPassports
#end check_pass_for_err function

#challenge:
# Count the number of valid passports - those that have all required fields. 
# Treat cid as optional. In your batch file, how many passports are valid?
validPassports = 0

#read the test puzzle input
#pass_file = open('day4_test_puzzle_input.txt', 'r')
#read the puzzle input
pass_file = open('day4_puzzle_input.txt', 'r')

#process the input file - a dictionary is returned
listofPassports = process_passports(pass_file)

#make list all passports into a dataframe to check content
df = pd.DataFrame(listofPassports)
passportsProcessed = len(df) # number of passports processed

#find passports with errors - i.e. missing information
errPassCount = check_pass_for_err(df)
validPassports = passportsProcessed - errPassCount

#print out the results
print()
print('number of valid passports: ', validPassports)
print('------------------------------------')
print('number of passports in total: ', passportsProcessed)
print('number of invalid passports: ', errPassCount)
print()
