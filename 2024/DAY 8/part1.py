with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

antennas = {} # stores the coords in a dict
antinodes = set()
MAX_ROW = len(lines)
MAX_COL = len(lines[0])

# parse the data
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j].isalnum():
            # this is an antenna
            if lines[i][j] in antennas:
                antennas[lines[i][j]].append((i, j))
            else:
                antennas[lines[i][j]] = [(i, j)]

for freq in antennas:
    coords = antennas[freq]
    for i in range(0, len(coords)):
        for j in range(i + 1, len(coords)):
            # find new antinodes

            displacement = (coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])

            new_anticode = (coords[i][0] + displacement[0], coords[i][1] + displacement[1])

            # ensure that the coords is within range
            if new_anticode[0] >= 0 and new_anticode[0] < MAX_ROW and new_anticode[1] >= 0 and new_anticode[1] < MAX_COL:
                antinodes.add(new_anticode)
            
            new_anticode = (coords[j][0] - displacement[0], coords[j][1] - displacement[1])

            if new_anticode[0] >= 0 and new_anticode[0] < MAX_ROW and new_anticode[1] >= 0 and new_anticode[1] < MAX_COL:
                antinodes.add(new_anticode)


# print(antinodes)
print(len(antinodes))