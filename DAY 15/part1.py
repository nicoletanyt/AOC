with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

seq = lines[0].split(",")
total = 0
for i in seq:
    val = 0
    for j in i:
        val += ord(j)
        val *= 17
        val = val % 256
    total += val

print(total)