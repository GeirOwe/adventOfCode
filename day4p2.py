# day 4 advent of code 2020
# by GeirOwe
# the challenge: https://adventofcode.com/2020/day/4
# part one of day 4 counts the invalid passports - the part two challenge counts the valid passports

import pandas as pd 

#process the input file and return a dataframe with all passports
def process_passports(pass_file):
    # passport information may span mre than one line in the input file - 
    # onePassport contains all the information on a passport
    onePassport = {}
    #process input - move passports a dictionary with one passport pr row
    listofPassports = []
    for onePass in pass_file:
        onePass = onePass.strip()
        #unless a blank line, the information on this line belongs to same passport as previous line
        if onePass == '':
            listofPassports.append(onePassport)
            onePassport = {}
        else:
            # Converting string from the input file into dictionary
            Dict = dict((x.strip(), y.strip()) 
                for x, y in (element.split(':')  
                for element in onePass.split(' ')))
            onePassport.update(Dict)
    # add the last row also - for some reason not included in loop
    listofPassports.append(onePassport)
    return listofPassports 
#end of process_passports function

#find passports with invalid data fields
def check_data_for_quality(df):
    #check data quality in birth year - byr. 
    # first convert from string to int
    df['byr'] = df['byr'].astype(int) 
    df = df[(df['byr'] >= 1920) & (df['byr'] <= 2002)] 
    
    #check data quality in issue year - iyr. 
    # first convert from string to int
    df['iyr'] = df['iyr'].astype(int) 
    df = df[(df['iyr'] >= 2010) & (df['iyr'] <= 2020)] 
    
    # check data quality in expiration year - eyr. 
    # first convert from string to int
    df['eyr'] = df['eyr'].astype(int) 
    df = df[(df['eyr'] >= 2020) & (df['eyr'] <= 2030)] 
    
    # split height in two columns
    # one for height and one for what measure is used; in or cm
    # then check data quality in height - hgt.  
    df['hgtn']=df.hgt.str.extract(r'(\d+)', expand = True)                          # extract numeric height from hgt - '\d+' means all the numbers
    df['hgtm']=df.hgt.str.extract('([a-zA-Z ]+)', expand = False)                   # extract if this is in or cm - 
    df['hgtn'] = df['hgtn'].astype(int)                                             # set new height column as int - [a-zA-Z ]+ means all the chars
    df = df[((df['hgtn'] >= 150) & (df['hgtn'] <= 193) & (df['hgtm'] == 'cm')) |    # If cm, the number must be at least 150 and at most 193.
    ( (df['hgtn'] >= 59) & (df['hgtn'] <= 76) & (df['hgtm'] == 'in') )]             # If in, the number must be at least 59 and at most 76.
    
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    df = df[df['hcl'].str.count(r'(^#\w{6}$)') == 1]                                # fields is to start with a '#' then followed six char or int, 

    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    df = df[df['ecl'].str.count(r'(^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$)') == 1]

    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    df = df[df['pid'].str.count(r'(^[0-9]{9}$)') == 1]           

    return df
#end of check_all_fields function

#find passports with errors - i.e. missing information
def check_pass_for_missing_data(df):
    # list all vald passports in a dataframe
    correctPassPorts = df[df['ecl'].notnull() & df['pid'].notnull() & df['eyr'].notnull() & df['hcl'].notnull() & df['byr'].notnull() & df['iyr'].notnull() & df['hgt'].notnull()]
  
    #the part two challenge - check that all data are within the rules for the fields
    correctPassPorts = check_data_for_quality(correctPassPorts)
  
    #number of valid passports
    validPassports = len(correctPassPorts)
    return validPassports
#end check_pass_for_missing_data function

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
df = pd.DataFrame(listofPassports)      #make list all passports into a dataframe to check content
passportsProcessed = len(df)            # number of passports processed

#find passports with errors - i.e. missing information
validPassports = check_pass_for_missing_data(df)
#validPassports = passportsProcessed - errPassCount

#print out the results
print()
print('number of valid passports: ', validPassports)
print('------------------------------------')
print('number of passports in total: ', passportsProcessed)
#print('number of invalid passports: ', errPassCount)
print()
