with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

# check through every X in the board in all directions to check for XMAS

total = 0
MAX_ROW = len(lines)
MAX_COL = len(lines[0])

def checkX(i, j):
    count = 0
    # extract strings for forward, backward, diagonal and reverse
    forward = lines[i][j:j+4]
    forward_reverse = forward[::-1]

    backward = lines[i][j - 3:j + 1]
    backward_reverse = backward[::-1]

    upward_reverse = "".join([l[j] for l in lines[i - 3:i + 1]])
    upward = upward_reverse[::-1]

    downward = "".join([l[j] for l in lines[i:i + 4]])
    downward_reverse = downward[::-1]

    diagonals = ["", "", "", ""]
    # diagonal bottom right. check if enough space to get diagonal 
    if MAX_ROW - i >= 4 and MAX_COL - j >= 4:
        for k in range(0, 4):
            diagonals[0] += lines[i + k][j + k]

    # diagonal top right
    if i >= 3 and MAX_COL - j >= 4:
        for k in range(0, 4):
            diagonals[1] += lines[i - k][j + k]
    
    # diagonal top left:
    if i >= 3 and j >= 3:
        for k in range(0, 4):
            diagonals[2] += lines[i - k][j - k]
    
    # diagonal bottom left
    if j >= 3 and MAX_ROW - i >= 4:
        for k in range(0, 4):
            diagonals[3] += lines[i + k][j - k]

    # print(diagonals)
    
    # check if these are valid by checking the length
    all_lines = diagonals + [forward, forward_reverse, backward, backward_reverse, upward, upward_reverse, downward, downward_reverse]
    for l in all_lines:
        if l == "XMAS":
            count += 1
    
    return count
    

for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j] == "X":
            total += checkX(i, j)

print(total)