# day3 of the advent of code
# by Geir Owe

#read the test puzzle input
#map_file = open('day3_test_puzzle_input.txt', 'r')

#read the puzzle input
map_file = open('day3_puzzle_input.txt', 'r')

#challenge:
# Starting at the top-left corner of your map and 
# following a slope of right 3 and down 1, how many trees would you encounter?

#where to start, what lane and how to move
absolutelyFirstLane = True
myPosition = 0
currentLane = 1

#count number of threes - ie. to get the answer to the puzzle
aThree = '#'
noOfThrees = 0

#in part two there are many scenarios for how much to move ahead and how many lanes to go down
move = 2
noOfLanesDown = 2
remainingLanesLeft = noOfLanesDown

#let´s get going - move ahead and stop; then go to next lane and check what's there
for lane in map_file:
    lane = lane.strip() #remove any trailing spaces or line-shift

    if absolutelyFirstLane: #first lane only, move ahead and prepare for next lane
        myPosition = myPosition + move
        absolutelyFirstLane = False
    else:
        #the lane is not a line - it's a circle
        if myPosition > (len(lane)-1): #since length of lane starts from 1 and myPosition starts from zero
            myPosition = 0 + (myPosition - len(lane)) 
        
        #you are now in the right position - prepare to go down to next lane
        currentLane = currentLane + 1 
        
        # only check the postion if you are in right lane - if not continue to next lane
        # you are at the right postion when remainingLanesLeft = 1
        if remainingLanesLeft == 1:
            #check for a three in the new position
            if lane[myPosition] == aThree: 
                noOfThrees = noOfThrees + 1
            
            myPosition = myPosition + move #move ahead
            remainingLanesLeft = noOfLanesDown # prepare for moving down again
        else:
            #one lane down
            remainingLanesLeft = remainingLanesLeft - 1

print('Number of threes in my way:', noOfThrees)
print('multiply together the number of trees in part two:', 82*242*71*67*24)