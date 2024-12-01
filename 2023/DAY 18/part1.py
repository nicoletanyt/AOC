with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

pos = (0, 0)
trench_pos = []

for i in range(0, len(lines)):
    parts = lines[i].split(" ")

    if parts[0] == "R":
        for j in range(1, int(parts[1]) + 1):
            trench_pos.append((pos[0], pos[1] + j))
    elif parts[0] == "L":
        for j in range(1, int(parts[1]) + 1):
            trench_pos.append((pos[0], pos[1] - j))
    elif parts[0] == "U":
        for j in range(1, int(parts[1]) + 1):
            trench_pos.append((pos[0] - j, pos[1]))
    elif parts[0] == "D":
        for j in range(1, int(parts[1]) + 1):
            trench_pos.append((pos[0] + j, pos[1]))
    pos = trench_pos[-1]

prev_row = trench_pos[0][0]

def shoelace(vertices):
    shoelace = 0
    for i in range(len(vertices) - 1):
        shoelace += vertices[i][0] * vertices[i + 1][1] - vertices[i + 1][0] * vertices[i][1]
    return abs(shoelace) // 2

print(shoelace(trench_pos) + len(trench_pos) // 2 + 1)