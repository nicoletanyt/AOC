from functools import reduce
import math

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

s = {}
t = []
curr = []

for i in range(2, len(lines)):
    l = lines[i].split(" = (")
    s[l[0]] = [l[1][0:3], l[1][5:8]]
    if l[0][-1] == "A":
        curr.append(l[0])

for j in range(0, len(curr)):
    r = False
    steps = 0
    while not r:
        for i in lines[0]:
            steps += 1
            if i == "R":
                curr[j] = s[curr[j]][1]
            else:
                curr[j] = s[curr[j]][0]

            if curr[j][-1] == "Z":
                t.append(steps)
                r = True

print(reduce(lambda x, y: x * y // math.gcd(x, y), t, 1))
