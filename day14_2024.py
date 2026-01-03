# 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 14, part 1 .... >')
    print()
    return

def process_the_data(robots):
    # Define the grid size
    #test grid
    #width = 11
    #height = 7
    #normal grid
    width = 101
    height = 103

    # Function to simulate robot movement
    def simulate_robots(robots, seconds):
        for _ in range(seconds):
            for robot in robots:
                # Update position based on velocity
                x = (robot['position'][0] + robot['velocity'][0]) % width
                y = (robot['position'][1] + robot['velocity'][1]) % height
                robot['position'] = (x, y)

    # Simulate for 100 seconds
    simulate_robots(robots, 100)

    # Count robots in each quadrant
    quadrant_counts = [0, 0, 0, 0]
    for robot in robots:
        x, y = robot['position']
        if x != width // 2 and y != height // 2: # Exclude middle lines
            if x < width // 2 and y < height // 2:
                quadrant_counts[0] += 1
            elif x >= width // 2 and y < height // 2:
                quadrant_counts[1] += 1
            elif x < width // 2 and y >= height // 2:
                quadrant_counts[2] += 1
            elif x >= width // 2 and y >= height // 2:
                quadrant_counts[3] += 1
    
    # Multiplying these quadrant_counts together gives a total safety factor
    total_safety = 1
    for quad in quadrant_counts:
        total_safety *= quad

    return total_safety

def get_the_data():
    # Open the input text file
    #with open("day14_2024_test_puzzle_input.txt", "r") as file:
    with open("day14_2024_puzzle_input.txt", "r") as file:
        # Parse each line into a dictionary with position and velocity
        robots = []
        for line in file:
            # Split the line into position and velocity parts
            parts = line.strip().split(" ")
            position = tuple(map(int, parts[0][2:].split(",")))  # Extract and convert position to tuple
            velocity = tuple(map(int, parts[1][2:].split(",")))  # Extract and convert velocity to tuple
            robots.append({'position': position, 'velocity': velocity})  # Append as a dictionary
    return robots

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('What will the safety factor be after exactly 100 seconds have elapsed? ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()