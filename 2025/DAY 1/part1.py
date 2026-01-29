with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

rotation = 50
count = 0
for l in lines:
    if l[0] == "L":
        rotation -= int(l[1:]) % 100
        if rotation < 0:
            rotation = 100 - abs(rotation)
    else:
        rotation += int(l[1:]) % 100
        if rotation > 99:
            rotation -= 100
    if rotation == 0:
        count += 1

print(count)
