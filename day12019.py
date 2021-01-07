#2019 day 1 Advent of Code

import os

#start function
def calc_fuel(thisModule):
    step_one = int(thisModule / 3)  #divide by 3 and round down
    fuel_needed = step_one - 2      #subtract 2
    if fuel_needed < 0:
        fuel_needed = 0
    return fuel_needed
#end function

#clear the console and start the programme
os.system('clear')
print('< .... AoC 2019 Day1 .... >')
print()

#let's start
if __name__ == '__main__':
    #read the test puzzle input
    #mass_file = open('day12019_test_puzzle_input.txt', 'r')
    #read the puzzle input
    mass_file = open('day12019_puzzle_input.txt', 'r')

    # Fuel required to launch a given module is based on its mass. 
    # Specifically, to find the fuel required for a module, take its 
    # mass, divide by three, round down, and subtract 2.
    total_fuel_required = 0

    #loop thru all items - calculate the fuel needed for the mass of each module 
    for module in mass_file:
        #remove any line-shift ans spaces and cnvert from str to int
        module = int(module.strip())
    
        #So, for each module mass, calculate its fuel and add it to the total. 
        fuel_needed = calc_fuel(module)
        total_fuel_required = total_fuel_required + fuel_needed
    
        # Then, treat the fuel amount you just calculated as the input mass and 
        # repeat the process, continuing until a fuel requirement is zero or negative.
        while fuel_needed > 0:
            fuel_needed = calc_fuel(int(fuel_needed))
            total_fuel_required = total_fuel_required + fuel_needed

    print('The total fuel requirement for the FCU, incl the mass of the added fuel, is: ', total_fuel_required)
    print()

