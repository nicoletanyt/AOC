with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

pos = (0, 0)
trench_pos = []

for i in range(0, len(lines)):
    parts = lines[i].split(" ")
    rgb = [int(x, 16) for x in parts[2][2:7]]

    dist = rgb[0] * 16 ** 4 + rgb[1] * 16 ** 3 + rgb[2] * 16 ** 2 + rgb[3] * 16 ** 1 + rgb[4]
    direc = parts[2][7]

    if direc == "0": # R
        for j in range(1, dist + 1):
            trench_pos.append((pos[0], pos[1] + j))
    elif direc == "2": # L
        for j in range(1, dist + 1):
            trench_pos.append((pos[0], pos[1] - j))
    elif direc == "3": # U
        for j in range(1, dist + 1):
            trench_pos.append((pos[0] - j, pos[1]))
    elif direc == "1": # D
        for j in range(1, dist + 1):
            trench_pos.append((pos[0] + j, pos[1]))
    
    pos = trench_pos[-1]

prev_row = trench_pos[0][0]

def shoelace(vertices):
    shoelace = 0
    for i in range(len(vertices) - 1):
        shoelace += vertices[i][0] * vertices[i + 1][1] - vertices[i + 1][0] * vertices[i][1]
    return abs(shoelace) // 2

print(shoelace(trench_pos) + len(trench_pos) // 2 + 1)