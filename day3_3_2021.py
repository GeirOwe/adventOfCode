# as found on reddit

get_vertical = lambda lst: [[y[x] for y in lst] for x in range(len(lst[0]))]
get_value = lambda x, n, m: n if x.count('0') > x.count('1') else m
calc_bin = lambda lst: int(''.join([str(x) for x in lst]), 2)

with open("day32021_puzzle_input.txt", 'r') as file: 
    data = file.read().splitlines()    
    gamma = [get_value(x, 0, 1) for x in get_vertical(data)]
    epsilon = [int(not(x)) for x in gamma]
    print("part1: ", calc_bin(gamma) * calc_bin(epsilon)) 
    oxy = data[:]
    co2 = data[:]
    for i,j in enumerate(data[0]):
        if len(oxy) > 1:
            current_oxy = get_value(get_vertical(oxy)[i], 0, 1)
            oxy = [x for x in oxy if int(x[i]) == current_oxy]
        if len(co2) > 1:
            current_co2 = get_value(get_vertical(co2)[i], 1, 0)
            co2 = [x for x in co2 if int(x[i]) == current_co2] 
    print("part1: ", calc_bin(oxy) * calc_bin(co2))

#let's start
#if __name__ == '__main__':
#    d03()