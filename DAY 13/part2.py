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

def check_h(c, lines, avail) -> bool:
    offset = 0
    while True:
        if c + offset + 1 == len(lines) or lines[c + offset + 1] == "" or c - offset - 2 < 0 or lines[c - offset - 2] == "":
            return True 
        elif lines[c + offset + 1] != lines[c - offset - 2]:
            # check if they are one off 
            if not avail:
                return False 
            elif avail and not checkDiff(lines[c + offset + 1], lines[c - offset - 2]):
                return False
        offset += 1

def checkDiff(s1, s2) -> bool:
    counter = 0
    if s1 == "" or s2 == "":
        return False
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            counter += 1
        if counter > 1:
            return False 
    return True

done = False 
s = 0 # start of pattern 
count = 0
store = []

for i in range(1, len(lines)): 
    if lines[i] == lines[i - 1]:
        # check for possible reflection, else continue 
        if check_h(i, lines, False):
            store.append((i - s) * 100)
            done = True 

    if lines[i] == '' or i == len(lines) - 1:
        if not done:
            # print("Vertical Reflection")
            pattern = get_v(s, i) 
            for k in range(1, len(pattern)):
                if pattern[k] == pattern[k - 1]:
                    if check_h(k, pattern, False):
                        store.append(k)
        
        # reset for next pattern
        s = i + 1
        done = False

s = 0
done = False 

print(store)

for i in range(1, len(lines)): 
    if not done:
        if lines[i] == lines[i - 1] or checkDiff(lines[i], lines[i - 1]):
            # check for possible reflection, else continue 
            if check_h(i, lines, True):
                if store[count] != (i - s) * 100:
                    # print(str((i - s) * 100) + " h")
                    count += 1
                    total += (i - s) * 100 # count 
                    done = True  

    if lines[i] == '' or i == len(lines) - 1:
        if not done:
            # print("Vertical Reflection")
            pattern = get_v(s, i) 
            for k in range(1, len(pattern)):
                if pattern[k] == pattern[k - 1] or checkDiff(pattern[k], pattern[k - 1]):
                    if check_h(k, pattern, True):
                        if store[count] != k:
                            # print(str(k) + "v")
                            count += 1
                            total += k 
                            break
        
        # reset for next pattern
        s = i + 1
        done = False
print(total) 