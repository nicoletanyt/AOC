with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

# MAX_ROW, MAX_COL = 7, 11
MAX_ROW, MAX_COL = 103, 101
grid = [[0 for _ in range(MAX_COL)] for _ in range(MAX_ROW)]
first, second, third, fourth = 0, 0, 0, 0

def moveRobot(pos, v):
    for _ in range(100):
        pos[0] += v[0]
        pos[1] += v[1]

        pos[0] %= MAX_ROW
        pos[1] %= MAX_COL

    return pos

# parse the data
for line in lines:
    parts = line.split(" ")
    pos = parts[0].replace("p=", "").split(",")
    # flip as x and y are different from rows and cols
    pos = [int(pos[1]), int(pos[0])]

    velocity = parts[1].replace("v=", "").split(",")
    velocity = (int(velocity[1]), int(velocity[0]))
    
    pos = moveRobot(pos, velocity)
    grid[pos[0]][pos[1]] += 1

for i in range(MAX_ROW):
    for j in range(MAX_COL):
        if i < 51 and j < 50:
            first += grid[i][j]
        elif i < 51 and j > 50:
            second += grid[i][j]
        elif i > 51 and j < 50:
            third += grid[i][j]
        elif i > 51 and j > 50:
            fourth += grid[i][j]

total = first * second * third * fourth
print(total)