# BRUTE FORCE

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

cube_rock_pos = []
single_rock_pos = []
total = 0
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
row_max = len(lines)
col_max = len(lines[0])

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if lines[i][j] == "#":
            cube_rock_pos.append((i, j))
        elif lines[i][j] == "O":
            single_rock_pos.append((i, j))

for n in range(0, 1000):
    for j in directions:
        if j == (-1, 0):
            single_rock_pos = sorted(single_rock_pos, key=lambda x : x[0])
        elif j == (0, -1):
            single_rock_pos = sorted(single_rock_pos, key=lambda x : x[1])
        elif j == (1, 0):
            single_rock_pos = sorted(single_rock_pos, key=lambda x : x[0], reverse=True)
        elif j == (0, 1):
            single_rock_pos = sorted(single_rock_pos, key=lambda x : x[1], reverse=True)

        for i in range(0, len(single_rock_pos)):
            while True:
                c = single_rock_pos[i]
                p = (c[0] + j[0], c[1] + j[1])
                if p in cube_rock_pos or p in single_rock_pos or p[0] < 0 or p[1] < 0 or p[0] == row_max or p[1] == col_max:
                    # stop moving if it hits any rock or reaches boundary
                    break 
                else:
                    # keep moving 
                    single_rock_pos[i] = p

for i in single_rock_pos:
    total += abs(i[0] - row_max)

print(total)