import math

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

ranges = lines[0].split(",")
total = 0

for r in ranges:
    first, second = r.split("-")
    first, second = int(first), int(second)

    for i in range(first, second + 1):
        id = str(i)
        length = len(id)
        if id[: math.floor(length / 2)] == id[int(length / 2) :]:
            total += i

print(sum)
