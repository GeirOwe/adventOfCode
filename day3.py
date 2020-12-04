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
myPosition = 0
currentLane = 1
move = 3
aThree = '#'
noOfThrees = 0

#let´s get going - move ahead and stop; then go to next lane and check what's there
for lane in map_file:
    lane = lane.strip() #remove any trailing spaces or line-shift
    if myPosition == 0:
        myPosition = myPosition + move
    else:
        #the lane is not a line - it's a circle
        if myPosition > (len(lane)-1): #since length of lane starts from 1 and myPosition starts from zero
            myPosition = 0 + (myPosition - len(lane)) 
        
        currentLane = currentLane + 1 #get down to next lane
        if lane[myPosition] == aThree:
            noOfThrees = noOfThrees + 1
            #if currentLane >= 100 and currentLane <= 105:
            #    print('row: ', currentLane)
            #    print('position: ', myPosition+1)
            #    print('what is here: ', lane[myPosition])
        myPosition = myPosition + move #move 3 ahead

print('Number of threes in my way:', noOfThrees)