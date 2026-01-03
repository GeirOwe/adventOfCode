# 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 12, part 1 .... >')
    print()
    return

def rotate_shape(shape):
    """Rotate shape 90 degrees clockwise."""
    rows = len(shape)
    cols = len(shape[0])
    rotated = [['.' for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - 1 - i] = shape[i][j]
    return rotated

def flip_shape(shape):
    """Flip shape horizontally."""
    return [row[::-1] for row in shape]

def get_all_variants(shape):
    """Get all rotations and flips of a shape."""
    variants = set()
    current = shape
    
    # Try all 4 rotations
    for _ in range(4):
        # Add current orientation
        shape_str = tuple(tuple(row) for row in current)
        variants.add(shape_str)
        
        # Add flipped version
        flipped = flip_shape(current)
        flipped_str = tuple(tuple(row) for row in flipped)
        variants.add(flipped_str)
        
        # Rotate for next iteration
        current = rotate_shape(current)
    
    return [list(list(row) for row in variant) for variant in variants]

def parse_shapes(data):
    """Parse shapes from input."""
    shapes = {}
    i = 0
    while i < len(data):
        line = data[i]
        # Check if this is a region line (contains 'x' before ':')
        if 'x' in line and ':' in line:
            break
        
        # Check if this is a shape definition (number followed by ':')
        if ':' in line and not 'x' in line.split(':')[0]:
            # Parse shape index
            shape_idx = int(line.split(':')[0])
            i += 1
            
            # Parse shape grid
            shape_lines = []
            while i < len(data) and data[i] and not ':' in data[i]:
                shape_lines.append(list(data[i]))
                i += 1
            
            if shape_lines:
                shapes[shape_idx] = shape_lines
            
            # Skip blank line if present
            if i < len(data) and data[i] == '':
                i += 1
        else:
            i += 1
    
    return shapes, i

def get_shape_cells(shape):
    """Get list of (row, col) positions where shape has '#'."""
    cells = []
    for i in range(len(shape)):
        for j in range(len(shape[0])):
            if shape[i][j] == '#':
                cells.append((i, j))
    return cells

def can_place(region, shape_cells, start_row, start_col, width, height):
    """Check if shape can be placed at given position."""
    for dr, dc in shape_cells:
        r, c = start_row + dr, start_col + dc
        if r < 0 or r >= height or c < 0 or c >= width:
            return False
        if region[r][c] != '.':
            return False
    return True

def place_shape(region, shape_cells, start_row, start_col, marker):
    """Place shape on region with given marker."""
    for dr, dc in shape_cells:
        r, c = start_row + dr, start_col + dc
        region[r][c] = marker

def remove_shape(region, shape_cells, start_row, start_col):
    """Remove shape from region."""
    for dr, dc in shape_cells:
        r, c = start_row + dr, start_col + dc
        region[r][c] = '.'

def solve_region(width, height, required_presents, all_shape_variants):
    """Try to fit all required presents using efficient backtracking with better pruning."""
    # Pre-compute all variant cells
    shape_variant_cells = {}
    for shape_idx, variants in all_shape_variants.items():
        shape_variant_cells[shape_idx] = [get_shape_cells(v) for v in variants]
    
    # Build presents list
    presents = []
    total_cells_needed = 0
    for shape_idx, count in enumerate(required_presents):
        for _ in range(count):
            cells_list = shape_variant_cells[shape_idx]
            cell_count = len(cells_list[0]) if cells_list else 0
            presents.append((shape_idx, cells_list, cell_count))
            total_cells_needed += cell_count
    
    if not presents:
        return True
    
    if total_cells_needed > width * height:
        return False
    
    # Sort by size (largest first) and constraint (more constrained first)
    presents.sort(key=lambda x: (-x[2], x[0]))
    
    # Use list for region (faster than set for small regions)
    region = [['.' for _ in range(width)] for _ in range(height)]
    
    def can_place(cells, r0, c0):
        """Check if shape can be placed."""
        for dr, dc in cells:
            r, c = r0 + dr, c0 + dc
            if r < 0 or r >= height or c < 0 or c >= width or region[r][c] != '.':
                return False
        return True
    
    def place(cells, r0, c0, marker):
        """Place shape."""
        for dr, dc in cells:
            region[r0 + dr][c0 + dc] = marker
    
    def unplace(cells, r0, c0):
        """Remove shape."""
        for dr, dc in cells:
            region[r0 + dr][c0 + dc] = '.'
    
    # Memoization for failed states (using region signature)
    memo = {}
    
    def backtrack(idx):
        if idx >= len(presents):
            return True
        
        shape_idx, cells_list, _ = presents[idx]
        
        # Try each variant
        for cells in cells_list:
            # Try positions
            for r in range(height):
                for c in range(width):
                    if can_place(cells, r, c):
                        place(cells, r, c, str(shape_idx))
                        
                        if backtrack(idx + 1):
                            return True
                        
                        unplace(cells, r, c)
        
        return False
    
    result = backtrack(0)
    return result

def process_the_data(theData):
    """Process the puzzle input and count regions that can fit all presents."""
    # Parse shapes
    shapes, regions_start = parse_shapes(theData)
    
    # Generate all variants (rotations/flips) for each shape
    all_shape_variants = {}
    for shape_idx, shape in shapes.items():
        all_shape_variants[shape_idx] = get_all_variants(shape)
    
    # Parse regions
    regions = []
    for i in range(regions_start, len(theData)):
        if 'x' in theData[i] and ':' in theData[i]:
            parts = theData[i].split(':')
            size_part = parts[0].strip()
            quantities_str = parts[1].strip() if len(parts) > 1 else ''
            quantities = list(map(int, quantities_str.split())) if quantities_str else []
            
            width, height = map(int, size_part.split('x'))
            regions.append((width, height, quantities))
    
    # Try to fit presents in each region
    successful_regions = 0
    for idx, (width, height, required_presents) in enumerate(regions):
        # Debug: show what we're trying to fit
        present_counts = [(i, count) for i, count in enumerate(required_presents) if count > 0]
        print(f"Region {idx+1}: {width}x{height}, presents: {present_counts}")
        
        if solve_region(width, height, required_presents, all_shape_variants):
            print(f"  -> Success!")
            successful_regions += 1
        else:
            print(f"  -> Failed")
    
    return successful_regions
    
    return successful_regions

def get_the_data():
    #read the puzzle input 
    theData = open('day12_2025_test_puzzle_input.txt', 'r')
    #theData = open('day12_2025_puzzle_input.txt', 'r')
    
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('How many of the regions can fit all of the presents listed? -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()