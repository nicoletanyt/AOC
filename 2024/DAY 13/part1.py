with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0

# parse the data
for i in range(0, len(lines), 4):
    parsedA = lines[i].replace("Button A: X+", "").replace(" Y+", "")
    A = [int(x) for x in parsedA.split(",")]

    parsedB = lines[i + 1].replace("Button B: X+", "").replace(" Y+", "")
    B = [int(x) for x in parsedB.split(",")]

    parsedPrize = lines[i + 2].replace("Prize: X=", "").replace(" Y=", "")
    prize = [int(x) for x in parsedPrize.split(",")]
    
    b = round((prize[1] - (prize[0]/A[0]) * A[1]) / (-(B[0] / A[0]) * A[1] + B[1]))
    
    a = round((prize[0] - B[0] * b) / A[0])

    if a * A[0] + b * B[0] == prize[0] and a * A[1] + b * B[1] == prize[1]:
        total += a * 3 + b

print(total)
    