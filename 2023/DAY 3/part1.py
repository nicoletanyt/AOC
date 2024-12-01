with open('DAY 3/input.txt') as f:
    lines = [line.rstrip() for line in f]

sum = 0
symbol_index = []
n = len(lines[0])

for i in range(0, len(lines)):
    for j in range(0, n):
        if not (lines[i][j].isalpha() or lines[i][j].isdigit() or lines[i][j] == "."):
            symbol_index.append(n * i + j)

num = ""
is_part = False 

for i in range(0, len(lines)):
    for j in range(0, n):
        if lines[i][j].isdigit():
            num += str(lines[i][j])
            if is_part == False:
                if (i * n + j + 1) in symbol_index or (i * n + j - 1) in symbol_index or (i * n + j + n) in symbol_index or (i * n + j - n) in symbol_index  or (i * n + j + 1 + n) in symbol_index  or (i * n + j - 1 + n) in symbol_index  or (i * n + j + 1 - n) in symbol_index  or (i * n + j - 1 - n) in symbol_index:
                    is_part = True
        else:
            if is_part == True:
                sum += int(num)
            is_part = False
            num = ""
            

print(sum)
            