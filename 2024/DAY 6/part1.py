with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

pos = 0 
total = 1 # including the starting pos
curr_dir = 0 # start by moving upwards
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
MAX_ROW = len(lines)
MAX_COL = len(lines[0])

def move(direction: tuple[int]):
    count = 0
    while True:
        if pos[0] == MAX_ROW - 1 or pos[1] == MAX_COL - 1 or pos[0] == 0 or pos[1] == 0 or lines[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            return count
        elif lines[pos[0] + direction[0]][pos[1]+ direction[1]] == ".":
            count += 1
            # mark as visited
            lines[pos[0] + direction[0]] = lines[pos[0] + direction[0]][:pos[1]+ direction[1]] + "X" + lines[pos[0] + direction[0]][pos[1]+ direction[1] + 1:]
        
        pos[0] += direction[0]
        pos[1] += direction[1]

# find the starting pos
for i in range(0, len(lines)):
    if "^" in lines[i]:
        pos = [i, lines[i].index("^")]

# starting from the start pos, loop until it reaches a boundary 
while True:
    total += move(DIRECTIONS[curr_dir])
    if pos[0] == MAX_ROW - 1 or pos[1] == MAX_COL - 1:
        break

    if curr_dir == 3:
        curr_dir = 0
    else:
        curr_dir += 1
  
print(total)