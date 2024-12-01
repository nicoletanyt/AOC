with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

time = lines[0].split(" ")
distance = lines[1].split("  ")
total = 1
nums = 0

for i in range(0, len(time)):
    possible = 0
    if time[i].isdigit():
        nums += 1
        for j in range(0, int(time[i])):
            # holding down for j ms 
            if (int(time[i]) - j) * j > int(distance[nums]):
                possible += 1
        total *= possible

print(total)