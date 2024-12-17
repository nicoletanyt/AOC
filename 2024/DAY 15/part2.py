with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

movement = ""
boxes = []
walls = []
pos = 2 + 1j
directions = {
    "<": -1j,
    "^": -1,
    ">": 1j,
    "v": 1
}
total = 0
x, y = 0, 0

def canMove(pos, move):
    # if there is a box here, see if can move the box in the same direction
    new_pos = pos + directions[move]
    if int(new_pos.real) < 0 or int(new_pos.real) >= MAX_ROW or int(new_pos.imag) < 0 or int(new_pos.imag) >= MAX_COL:
        # out of bounds
        return False
    
    if new_pos in walls:
        # cannot move, so nothing happens
        return False
    
    # find if this is a box
    for i in range(len(boxes)):
        if new_pos == boxes[i][0] or new_pos == boxes[i][1]:
            # this is a box, see if can move this
            if move == "<" or move == ">":
                return canMove(new_pos, move)
            else:
                return canMove(boxes[i][0], move) and canMove(boxes[i][1], move)

    return True

def moveBox(new_pos, move):
    for i in range(len(boxes)):
        if new_pos == boxes[i][0]:
            # this is part of a box, move the box at this new_pos
            if move == ">" or move == "<":
                moveBox(boxes[i][0] + directions[m], move)
                boxes[i][0] += directions[m]
            else:
                # move both parts of the box if up or down    
                moveBox(boxes[i][0] + directions[m], move)
                boxes[i][0] += directions[m]

                moveBox(boxes[i][1] + directions[m], move)
                boxes[i][1] += directions[m]

        if new_pos == boxes[i][1]:
            if move == ">" or move == "<":
                moveBox(boxes[i][1] + directions[m], move)
                boxes[i][1] += directions[m]
            else:
                # move this and first part of box
                moveBox(boxes[i][1] + directions[m], move)
                boxes[i][1] += directions[m]

                moveBox(boxes[i][0] + directions[m], move)
                boxes[i][0] += directions[m]


# parse data
for i in range(0, len(lines)):
    if lines[i] == "":
        # movements
        movement = "".join(lines[i + 1:])
        MAX_ROW = i
        break
    else:
        # grid
        for j in range(len(lines[i])):
            if lines[i][j] == "O":
                boxes.append([complex(x, y), complex(x, y + 1)])
            elif lines[i][j] == "@":
                pos = complex(x, y)
            elif lines[i][j] == "#":
                walls.append(complex(x, y))
                walls.append(complex(x, y + 1))
            
            y += 2
    x += 1
    MAX_COL = y
    y = 0

MAX_ROW = x

for m in movement:
    if canMove(pos, m):
        # move robot 
        pos += directions[m]
        moveBox(pos, m)

# calculate GPS
for i in boxes:
    total += (int(i[0].real) * 100 + int(i[0].imag))

print(total)
