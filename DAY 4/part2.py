with open('DAY 4/input.txt') as f:
    lines = [line.rstrip() for line in f]

winning_nums = []
total_copies = [1] * len(lines)

for i in range(0, len(lines)):
    cards = lines[i].split(": ")[1].split(" | ")
    winning = cards[0].split(" ")
    yours = cards[1].split(" ")
    count = 0
    for j in yours:
        if j in winning and j.isdigit():
            count += 1
    
    winning_nums.append(count)
    

for i in range(0, len(winning_nums)):
    for j in range(0, winning_nums[i]):
        total_copies[j + i + 1] += total_copies[i]

print(sum(total_copies))