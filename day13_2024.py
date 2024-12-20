# 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 13, part 1 .... >')
    print()
    return

def parse_puzzle_input(file_path):
    puzzles = []
    with open(file_path, 'r') as file:
        puzzle = {}
        for line in file:
            line = line.strip()
            if line:
                if line.startswith('Button A:'):
                    parts = line.split(',')
                    puzzle['button_a_x'] = int(parts[0].split('+')[1])
                    puzzle['button_a_y'] = int(parts[1].split('+')[1])
                elif line.startswith('Button B:'):
                    parts = line.split(',')
                    puzzle['button_b_x'] = int(parts[0].split('+')[1])
                    puzzle['button_b_y'] = int(parts[1].split('+')[1])
                elif line.startswith('Prize:'):
                    parts = line.split(',')
                    puzzle['prize_x'] = int(parts[0].split('=')[1])
                    puzzle['prize_y'] = int(parts[1].split('=')[1])
                    puzzles.append(puzzle)
                    puzzle = {}
    return puzzles

# Function to solve the puzzle (from the previous answer)
def solve_claw_puzzle(prize_x, prize_y, button_a_x, button_a_y, button_b_x, button_b_y):
    # You estimate that each button would need to be pressed no more than 100 times to win 
    # a prize. How else would someone be expected to play?
    for a in range(100):
        for b in range(100):
            x = a * button_a_x + b * button_b_x
            y = a * button_a_y + b * button_b_y
            if x == prize_x and y == prize_y:
                return a, b
    return None, None

def process_the_data(theData):
    # Solve each puzzle
    total_cost = 0
    for i, puzzle in enumerate(theData, 1):
        a_presses, b_presses = solve_claw_puzzle(**puzzle)
        # calculate cost
        # it costs 3 tokens to push the A button and 1 token to push the B button.
        if a_presses is not None and b_presses is not None:
            total_cost = total_cost + (a_presses * 3) + (b_presses * 1)

    return total_cost

def get_the_data():
    #read the test puzzle input
    #theData = parse_puzzle_input('day13_2024_test_puzzle_input.txt')
    #read the puzzle input 
    theData = parse_puzzle_input('day13_2024_puzzle_input.txt')
    return theData

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('What is the fewest tokens you would have to spend to win all possible prizes? ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()