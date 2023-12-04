with open('DAY 4/input.txt') as f:
    lines = [line.rstrip() for line in f]

sum = 0

for i in lines:
    cards = i.split(": ")[1].split(" | ")
    winning = cards[0].split(" ")
    yours = cards[1].split(" ")
    points = 0
    for j in yours:
        if j in winning and j.isdigit():
            if points == 0:
                points = 1
            else:
                points *= 2
            winning.remove(j)
    sum += points

print(sum)