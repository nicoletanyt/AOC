with open('input.txt') as f:
    data = [line for line in f]

data = [int(n) for n in data[0]]

total = 0
files = []
filled = []
n = 0

for i in range(0, len(data)):
    if i % 2 == 1:
        # block of empty space
        for j in range(data[i]):
            # add this to the 
            files.append(-1)
    else:
        # this is a block of file
        for j in range(data[i]):
            # add this to the 
            files.append(i // 2)
            filled.append(len(files) - 1)

count = len(filled)

for i in range(0, len(files)):
    if n == count:
        # finished moving
        break
    if files[i] >= 0:
        total += i * files[i]
    else:
        # empty space, get the number from the back
        total += i * files[filled[-1]]
        # removes last element 
        filled.pop()
    n += 1

print(total)