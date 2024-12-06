with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTION_SYMBOLS = ["^", ">", "|", "<"]
MAX_ROW = len(lines)
MAX_COL = len(lines[0])
START = []

pos = 0 
total = 0 # including the starting pos
curr_dir = 0 # start by moving upwards
visited = set()

def move(direction: tuple[int]):
    while True:
        if pos[0] == MAX_ROW - 1 or pos[1] == MAX_COL - 1 or pos[0] == 0 or pos[1] == 0 or lines[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            break
        elif lines[pos[0] + direction[0]][pos[1]+ direction[1]] == ".":
            # mark as visited
            visited.add((pos[0] + direction[0], pos[1]+ direction[1]))
        
        pos[0] += direction[0]
        pos[1] += direction[1]

# find the starting pos
for i in range(0, len(lines)):
    if "^" in lines[i]:
        pos = [i, lines[i].index("^")]
        START = [i, lines[i].index("^")]
        break

# starting from the start pos, loop until it reaches a boundary 
while True:
    move(DIRECTIONS[curr_dir])
    if pos[0] == MAX_ROW - 1 or pos[1] == MAX_COL - 1:
        break

    if curr_dir == 3:
        curr_dir = 0
    else:
        curr_dir += 1

def checkX(start_pos: list[int], board):
     curr_dir = 0
     curr_pos = start_pos.copy()

     while True:
        direction = DIRECTIONS[curr_dir]
        while True:
            if curr_pos[0] == MAX_ROW - 1 or curr_pos[1] == MAX_COL - 1 or curr_pos[0] == 0 or curr_pos[1] == 0:
                # not possible because it reached the boundary
                return False
            elif board[curr_pos[0] + direction[0]][curr_pos[1] + direction[1]] == "#":
                break
            elif board[curr_pos[0] + direction[0]][curr_pos[1] + direction[1]] == ".":
                # update direction
                board[curr_pos[0] + direction[0]] = board[curr_pos[0] + direction[0]][:curr_pos[1]+ direction[1]] + DIRECTION_SYMBOLS[curr_dir] + board[curr_pos[0] + direction[0]][curr_pos[1]+ direction[1] + 1:]
            else:
                # has already been here, check if it's the same direction
                if board[curr_pos[0] + direction[0]][curr_pos[1] + direction[1]] == DIRECTION_SYMBOLS[curr_dir]:
                    # has already been here and will continue in same direction 
                    return True

            # keep moving
            curr_pos[0] += direction[0]
            curr_pos[1] += direction[1]
            
        if curr_dir == 3:
            curr_dir = 0
        else:
            curr_dir += 1
     
# go through all the X positions and check if that is an obstacle, will it still work 
for i in visited:
    lines_cpy = lines.copy()
    lines_cpy[i[0]] = lines_cpy[i[0]][:i[1]] + "#" + lines_cpy[i[0]][i[1] + 1:]
    
    if checkX(START, lines_cpy):
        total += 1

print(total)    

# if it goes past two visited in a row, it's a loop 