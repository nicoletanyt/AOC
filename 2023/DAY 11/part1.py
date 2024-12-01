with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

board = []

# check rows for expansion 
for i in lines:
    expand = True  
    for j in i:
        if j == "#":
            expand = False 
            break
    if expand:
        board.append(i)
    board.append(i)

col_index = []
for i in range(0, len(lines[0])):
    expand = True
    for j in range(0, len(lines)):
        if lines[j][i] == "#":
            expand = False 
            break
    if expand:
        col_index.append(i)
            
for j in range(0, len(board)):
    for i in range(0, len(col_index)):
        board[j] = board[j][:col_index[i] + i] + "." + board[j][col_index[i] + i:]

galaxy = [] # (row, col) coords of stars 
dist_sum = 0 

for i in range(0, len(board)):
    for j in range(0, len(board[i])):
        if board[i][j] == "#":
            galaxy.append((i, j)) 

print(galaxy)

for i in range(0, len(galaxy)):
    for j in range(i, len(galaxy)):
        dist = abs(galaxy[i][0] - galaxy[j][0]) + abs(galaxy[i][1] - galaxy[j][1])
        print(dist)
        dist_sum += dist

print(dist_sum)