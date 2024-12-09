with open('input.txt') as f:
    data = [line for line in f]

data = [int(n) for n in data[0]]

total = 0
files = []
empty = []

for i in range(0, len(data)):
    if i % 2 == 1:
        # block of empty space
        if data[i] > 0:
            empty.append([len(files), data[i]])
        for j in range(data[i]):
            files.append(-1)
    else:
        # this is a block of file
        for j in range(data[i]):
            files.append(i // 2)

curr = len(files) - 1

# start looping from the back 
for i in range(len(data) - 1, -1, -1):
    if i % 2 == 0:
        # block of files, see if can move in front
        for k in range(0, len(empty)):
            [start, count] = empty[k]
            if count >= data[i] and start < curr:
                # can fit at the front, so move 
                for j in range(0, data[i]):
                    files[start + j] = i // 2
                    files[curr - j] = -1
                
                if count == data[i]:
                    # no more empty space, so remove this from the array
                    empty.remove(empty[k])
                else:
                    # edit the element
                    empty[k] = [start + data[i], count - data[i]]
                break
    
    curr -= data[i]

for i in range(0, len(files)):
    if files[i] > 0:
        total += i * files[i]

print(total)