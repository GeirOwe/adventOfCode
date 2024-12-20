# day2 of the advent of code challenge
# by GeirOwe

#start function
def split_string(firstLine):

    #split the line at column. left part, xxx.[0], is the two numbers and the letter to look for
    #right part, xxx.[1], is the password. we strip it to remove any leading / trailing spaces 
    lineDict = firstLine.split(':')
    pw = lineDict[1].strip()

    #then we split the left part, xxx.[0], one more time
    numbersAndChar = lineDict[0].split('-')
    #left part, [0], contains the first number
    firstNo = numbersAndChar[0]

    #then we split the right part one more time
    lastNumber = numbersAndChar[1].split(' ')
    #left part, zzz.[0], is the second number
    secondNo = lastNumber[0]
    #right part, zzz.[1], is the letter to look for
    letterToLookFor = lastNumber[1]

    return firstNo, secondNo, letterToLookFor, pw
#end split_string function

#start function
def check_pw(firstNo, secondNo, letterToLookFor, pw):
    #check number of times the letter to look for is in password
    count = 0
    for i in pw:
        if i == letterToLookFor:
            count = count + 1
    
    #check if the count is within the range of first and second number
    if count >= firstNo and count <= secondNo:
        return 1
    else:
        return 0
#end check_pw function

#read the puzzle input
pw_file = open('day2_puzzle_input.txt', 'r')
#How many passwords are valid according to their policies? pwCount holds the number
pwCount = 0

#read a line and loop until all lines are read
for line in pw_file:
    #call the split string function
    a, b, c, d = split_string(line)
    
    #check the password
    result = check_pw(int(a), int(b), c, d)
    
    pwCount = pwCount + result

print('number of valid passwords: ', pwCount)
