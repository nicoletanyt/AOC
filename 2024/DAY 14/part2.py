# input.txt
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

# MAX_ROW, MAX_COL = 7, 11
MAX_ROW, MAX_COL = 103, 101
robots = []
answer = 0

def moveRobot(pos, v, seconds):
    new_pos = pos.copy()
    for _ in range(seconds):
        new_pos[0] += v[0]
        new_pos[1] += v[1]

        new_pos[0] %= MAX_ROW
        new_pos[1] %= MAX_COL

    return new_pos

def displayGrid(grid):
    for i in grid:
        s = "".join(i)
        print(s)

    print()

# parse the data
for line in lines:
    parts = line.split(" ")
    pos = parts[0].replace("p=", "").split(",")
    # flip as x and y are different from rows and cols
    pos = [int(pos[1]), int(pos[0])]

    velocity = parts[1].replace("v=", "").split(",")
    velocity = (int(velocity[1]), int(velocity[0]))
    
    robots.append([pos, velocity])

# find the longest string of "X" to find the horizontal border of the box
for second in range(10000):
    grid = [["." for _ in range(MAX_COL)] for _ in range(MAX_ROW)]
    for r in range(len(robots)):
        pos = moveRobot(robots[r][0], robots[r][1], second)
        if grid[pos[0]][pos[1]] == "X":
            # cannot be the answer as two robots share the same location
            break
        grid[pos[0]][pos[1]] = "X"

        if r == len(robots) - 1:      
            answer = second      
            break

print(answer) 
displayGrid(grid)