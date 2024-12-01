with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

time = lines[0].split(":")[1].replace(" ", "")
distance = lines[1].split(":")[1].replace(" ", "")
total = 0

for j in range(0, int(time)):
    # holding down for j ms 
    if (int(time) - j) * j > int(distance):
        total += 1

print(total)