with open('DAY 3/input.txt') as f:
    lines = [line.rstrip() for line in f]

sum = 0
symbol_index = {}
n = len(lines[0])

for i in range(0, len(lines)):
    for j in range(0, n):
        if lines[i][j] == "*":
            symbol_index[n * i + j] = []

num = ""
is_part = False 
index = 0

for i in range(0, len(lines)):
    for j in range(0, n):
        if lines[i][j].isdigit():
            num += str(lines[i][j])
            if is_part == False:
                for k in list(symbol_index.keys()):
                    # for optimisation, don't use symbol_index and just check if this == "*"
                    if (i * n + j + 1) == k or (i * n + j - 1) == k or (i * n + j + n) == k or (i * n + j - n) == k  or (i * n + j + 1 + n) == k  or (i * n + j - 1 + n) == k  or (i * n + j + 1 - n) == k  or (i * n + j - 1 - n) == k:
                        is_part = True
                        index = k
                        break
        else:
            if is_part:
                symbol_index[index].append(int(num))
            is_part = False
            num = ""
            index = 0

for i in symbol_index:
    product = 1
    if len(symbol_index[i]) == 2:
        for j in symbol_index[i]:
            product *= j 
        sum += product

print(sum)
