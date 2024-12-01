with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

s = {}
steps = 0

for i in range(2, len(lines)):
    l = lines[i].split(" = (")
    s[l[0]] = [l[1][0:3], l[1][5:8]]

curr = "AAA"

while curr != "ZZZ":
    for i in lines[0]:
        if i == "R":
            curr = s[curr][1]
        else:
            curr = s[curr][0]
        steps += 1

        if curr == "ZZZ":
            break

print(steps)    

