with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

board = []
multiple = 1000000
expand_str = "." * (multiple - 1)
galaxy = [] # (row, col) coords of stars 
dist_sum = 0

row_expanded = 0

# check rows for expansion 
for i in range(0, len(lines)):
    expand = True  
    for j in range(0, len(lines[i])):
        if lines[i][j] == "#":
            expand = False 
            galaxy.append((i + (row_expanded * (multiple - 1)), j))
    if expand:
        row_expanded += 1
        for k in range(0, multiple - 1):
            board.append(lines[i])
    board.append(lines[i])

col_index = [] 

for i in range(0, len(board[0])):
    expand = True
    for j in range(0, len(board)):
        if board[j][i] == "#":
            expand = False 
            break
    if expand:
        col_index.append(i) 

print(col_index)

for i in range(0, len(galaxy)):
    for j in range(i, len(galaxy)):
        offset = 0
        for k in col_index:
            big = max(galaxy[i][1], galaxy[j][1])
            small = min(galaxy[i][1], galaxy[j][1])
            if (big >= k and k >= small):
                # in range
                offset += (multiple - 1)
        dist = abs(galaxy[i][0] - galaxy[j][0]) + abs(galaxy[i][1] - galaxy[j][1]) + offset
        dist_sum += dist

print(dist_sum)