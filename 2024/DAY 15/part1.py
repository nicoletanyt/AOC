with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

MAX_ROW = len(lines)
MAX_COL = len(lines[0])
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

def canMove(pos, move):
    # if there is a box here, see if can move the box in the same direction
    new_pos = pos + directions[move]
    if int(new_pos.real) < 0 or int(new_pos.real) >= MAX_ROW or int(new_pos.imag) < 0 or int(new_pos.imag) >= MAX_COL:
        # out of bounds
        return False
    if new_pos in boxes:
        # see if can move the box 
        return canMove(new_pos, move)
    elif new_pos in walls:
        # cannot move, so nothing happens
        return False
    else:
        return True

def moveBox(new_pos, move):
    if new_pos in boxes:
        # move the box at this new_pos
        n = boxes.index(new_pos)
        moveBox(boxes[n] + directions[m], move)
        boxes[n] += directions[m]

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
                boxes.append(complex(i, j))
            elif lines[i][j] == "@":
                pos = complex(i, j)
            elif lines[i][j] == "#":
                walls.append(complex(i, j))

for m in movement:
    if canMove(pos, m):
        # move robot 
        pos += directions[m]
        moveBox(pos, m)

# calculate GPS
for i in boxes:
    total += (int(i.real) * 100 + int(i.imag))

print(total)
