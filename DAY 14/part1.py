with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

cube_rock_pos = []
single_rock_pos = []
total = 0

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if lines[i][j] == "#":
            cube_rock_pos.append((i, j))
        elif lines[i][j] == "O":
            single_rock_pos.append((i, j))

for i in range(0, len(single_rock_pos)):
    while True:
        c = single_rock_pos[i]
        # print(c)
        if (c[0] - 1, c[1]) in cube_rock_pos or (c[0] - 1, c[1]) in single_rock_pos or c[0] == 0:
            # stop moving if it hits any rock or reaches boundary
            break 
        else:
            # keep moving down 
            single_rock_pos[i] = (c[0] - 1, c[1])

for i in single_rock_pos:
    total += abs(i[0] - 100)

print(total)