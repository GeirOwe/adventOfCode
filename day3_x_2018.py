# Day3 - 2018 Advent of code - ChatGPT version
# source: https://adventofcode.com/2018

def parse_claim(claim):
    # Parse a claim string and return the ID, left margin, top margin, width, and height
    parts = claim.split()
    claim_id = int(parts[0][1:])
    left_margin, top_margin = map(int, parts[2][:-1].split(','))
    width, height = map(int, parts[3].split('x'))
    return claim_id, left_margin, top_margin, width, height

def mark_claims(claims, fabric):
    # Mark claimed areas on the fabric grid
    for claim in claims:
        _, left, top, width, height = claim
        for i in range(left, left + width):
            for j in range(top, top + height):
                fabric[i][j] += 1

def count_overlapping_inches(fabric):
    # Count the number of square inches with multiple claims
    count = 0
    for row in fabric:
        for cell in row:
            if cell > 1:
                count += 1
    return count

def main():
    # Read claims from input
    with open("day32018_puzzle_input.txt", "r") as file:
        claims = [parse_claim(line.strip()) for line in file]

    # Find the size of the fabric grid
    max_width = max(claim[1] + claim[3] for claim in claims)
    max_height = max(claim[2] + claim[4] for claim in claims)

    # Initialize fabric grid with zeros
    fabric = [[0] * max_height for _ in range(max_width)]

    # Mark claims on the fabric
    mark_claims(claims, fabric)

    # Count overlapping square inches
    result = count_overlapping_inches(fabric)

    print("Square inches within two or more claims:", result)

if __name__ == "__main__":
    main()

