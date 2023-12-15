with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

# read data 
data = []
s_pos = (0, 0) # (row num, col num) coords

for i in range(0, len(lines)):
    row = []
    for j in range(0, len(lines[i])):
        row.append(lines[i][j])
        if lines[i][j] == "S":
            s_pos = (i, j)
    data.append(row)

direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
chars = {
    "|": [(1, 0), (-1, 0)], # each r bi-directional
    "-": [(0, 1), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}

routes = [] 
visited = []

def checkDir(pos):
    try:
        p_char = data[pos[0]][pos[1]]
        if p_char in chars:
            for i in chars[p_char]:
                if data[i[0] + pos[0]][i[1] + pos[1]] in chars and (i[0] + pos[0], i[1] + pos[1]) not in visited:
                    pos = (i[0] + pos[0], i[1] + pos[1])
                    if pos[0] >= 0 and pos[1] >= 0:
                        # print(pos)
                        visited.append(pos)   
                        return pos
                elif data[i[0] + pos[0]][i[1] + pos[1]] == "S":
                    return s_pos
    except:
        return pos

# check 4 dir from S
for i in direc:
    if data[i[0] + s_pos[0]][i[1] + s_pos[1]] in chars and (i[0] + s_pos[0], i[1] + s_pos[1]) not in visited:
        pos = (i[0] + s_pos[0], i[1] + s_pos[1])
        if pos[0] >= 0 and pos[1] >= 0:
            routes.append(pos)

steps = 0 # accounting for the side of the s_pos 
max_steps = 0

for i in range(0, len(routes)):
    pos = routes[i]
    steps += 1 
    visited.append(pos)
    while pos != s_pos:
        pos = checkDir(pos)
        if pos == s_pos:
            # start new possible route from the other side 
            visited = []
            max_steps = max(max_steps, int(steps/2))
            steps = 1 
        else:
            steps += 1

print(max_steps)