sum = 0

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

for i in lines:
    num = ""
    for j in range(0, len(i)):
        if i[j].isnumeric():
            num += i[j]
            break

    for j in range(len(i) - 1, -1, -1):
        if i[j].isnumeric():
            num += i[j]
            break

    sum += int(num)

print(sum)