with open('DAY 2/input.txt') as f:
    lines = [line.rstrip() for line in f]

sum = 0

# process input
for i in range(0, len(lines)):
    games = lines[i].split(": ")[1].split("; ")
    maximum = {
        "r": 0,
        "g": 0,
        "b": 0,
    }
    power = 0
    for k in games:
        vals = k.split(" ")
        for j in range(0, len(vals), 2):
            maximum[vals[j + 1][0]] = max(maximum[vals[j + 1][0]], int(vals[j]))
    
    sum += (maximum["r"] * maximum["g"] * maximum["b"])
    

print(sum)