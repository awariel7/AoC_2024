# read file
with open("data.txt", "r") as file:
    map = [[l for l in line.rstrip()] for line in file]

antennas_dict = {}
R = len(map)
C = len(map[0])
# create a dict of all antennas in the field
for i in range(R):
    for j in range(C):
        a = map[i][j]
        if a.isalnum():  # Check, whether current symbol is digit or letter
            if a not in antennas_dict:
                antennas_dict[a] = [(i, j)]
            else:
                antennas_dict[a].append((i, j))
# Part 1
antinodes_set = set()
# Part 2
antinodes_set_2 = set()
# calc antinodes positions for every antenna
for k in antennas_dict.keys():
    positions = antennas_dict[k]
    for p in positions:
        # compare with other antennas with the same frequency
        for i in range(len(positions)):
            # don't compare with itself
            if p == positions[i]:
                continue
            else:
                # diff
                x = p[0] - positions[i][0]
                y = p[1] - positions[i][1]
                # Part 2
                c1 = 1
                # Antennas itself will be an antinode
                antinodes_set_2.add((p[0], p[1]))
                antinodes_set_2.add((positions[i][0], positions[i][1]))
                while 0 <= p[0] + x * c1 < R and 0 <= p[1] + y * c1 < C:
                    # Part 1. Add 2 antinodes for each pair
                    if c1 == 1:
                        # antinode_pos_1
                        antinodes_set.add((p[0] + x * c1, p[1] + y * c1))
                        antinodes_set_2.add((p[0] + x * c1, p[1] + y * c1))
                    # Part 2. Add antinodes along the line
                    antinodes_set_2.add((p[0] + x * c1, p[1] + y * c1))
                    c1 +=1
                c2 = 1
                while 0 <= positions[i][0] - x * c2 < R and 0 <= positions[i][1] - y * c2 < C:
                    if c2 == 1:
                        # antinode_pos_2
                        antinodes_set.add((positions[i][0] - x * c2, positions[i][1] - y * c2))
                        antinodes_set_2.add((positions[i][0] - x * c2, positions[i][1] - y * c2))
                    antinodes_set_2.add((positions[i][0] - x * c2, positions[i][1] - y * c2))
                    c2 +=1

print(f'Part 1: {len(antinodes_set)}')
print(f'Part 2: {len(antinodes_set_2)}')
