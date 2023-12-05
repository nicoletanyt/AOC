with open('DAY 5/input.txt') as f:
    lines = [line.rstrip() for line in f]

seeds = lines[0].split(" ")
seeds.remove("seeds:")
lines.remove(lines[0])
min_location = 1000000000000
skip = False 

for j in range(0, len(seeds)):
    prev = int(seeds[j])
    for i in range(0, len(lines)):
        if not skip:
            if lines[i] == "":
                continue
            if lines[i][0].isdigit():
                coords = lines[i].split(" ")
                if int(coords[1]) + int(coords[2]) >= prev and int(coords[1]) <= prev:
                    prev = int(coords[0]) - int(coords[1]) + prev
                    skip = True 
        
        if "map" in lines[i]:
            skip = False 
            
    min_location = min(min_location, prev)

print(min_location)