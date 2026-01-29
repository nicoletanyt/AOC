import math

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

rotation = 50
count = 0

for l in lines:
    num = int(l[1:])
    count += math.floor(num / 100)
    prevRotation = rotation
    if l[0] == "L":
        rotation -= num % 100
        if rotation < 0:
            rotation = 100 - abs(rotation)
            if prevRotation != 0:
                count += 1
        elif rotation == 0:
            count += 1
    else:
        rotation += num % 100
        if rotation > 99:
            rotation -= 100
            if prevRotation != 0:
                count += 1

print(count)
