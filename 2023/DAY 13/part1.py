with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0

def get_v(s, e) -> [[]]:
    cols = []
    for i in range(0, len(lines[s])):
        col = ""
        for j in range(s, e):
            col += lines[j][i]
        cols.append(col)

    return cols

def check_h(c, lines) -> bool:
    offset = 0
    while True:
        if c + offset + 1 == len(lines) or lines[c + offset + 1] == "" or c - offset - 2 < 0 or lines[c - offset - 2] == "":
            return True 
        elif lines[c + offset + 1] != lines[c - offset - 2]:
            return False 
        offset += 1


done = False 
s = 0 # start of pattern 

for i in range(1, len(lines)): 
    if lines[i] == lines[i - 1]:
        # check for possible reflection, else continue 
        if check_h(i, lines):
            total += (i - s) * 100 # count 
            done = True 

    if lines[i] == '' or i == len(lines) - 1:
        if not done:
            # print("Vertical Reflection")
            pattern = get_v(s, i) 
            for k in range(1, len(pattern)):
                if pattern[k] == pattern[k - 1]:
                    if check_h(k, pattern):
                        total += k 
        
        # reset for next pattern
        s = i + 1
        done = False

print(total) 