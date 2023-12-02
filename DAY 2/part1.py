with open('DAY 2/input.txt') as f:
    lines = [line.rstrip() for line in f]

maximum = {
    "r": 12,
    "g": 13,
    "b": 14,
}

sum = 0

# process input
for i in range(0, len(lines)):
    possible = True 
    games = lines[i].split(": ")[1].split("; ")
    for k in games:
        vals = k.split(" ")
        for j in range(0, len(vals), 2):
            if int(vals[j]) > maximum[vals[j + 1][0]]:
                possible = False 
                break
    
    if possible:
        sum += (i + 1)

print(sum)