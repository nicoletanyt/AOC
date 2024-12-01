with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

x = 0

for i in range(0, len(lines)):
    nums = lines[i].split(" ")
    
    temp = nums
    x += int(nums[-1])
    while temp != [0] * len(temp):
        seq = []
        for j in range(0, len(temp) - 1):
            seq.append(int(temp[j + 1]) - int(temp[j]))

        temp = seq
        x += int(temp[-1])

print(x)