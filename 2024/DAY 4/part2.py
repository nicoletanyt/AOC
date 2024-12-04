with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

# check through every A in the board to find a possible MAS

total = 0

def checkA(i, j):
    # check diagonal 
    diagonal_downward = lines[i - 1][j - 1] + lines[i + 1][j + 1]
    diagonal_upward = lines[i + 1][j - 1] + lines[i - 1][j + 1]

    # valid X-MAS
    return ((diagonal_downward == "MS" or diagonal_downward == "SM") and (diagonal_upward == "MS" or diagonal_upward == "SM"))

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        if lines[i][j] == "A":
            total += checkA(i, j)

print(total)