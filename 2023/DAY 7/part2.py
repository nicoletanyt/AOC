from functools import cmp_to_key

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"] # larger index, weaker
rank = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: []
}

for i in lines:
    hand = i.split(" ")
    temp = {}
    J_count = 0
    for j in range(0, len(hand[0])):
        if hand[0][j] != "J":
            if hand[0][j] in temp:
                temp[hand[0][j]] += 1
            else:
                temp[hand[0][j]] = 1
        else:
            J_count += 1
    vals = list(temp.values())

    if J_count != 0:
        if J_count == 5:
            vals.append(5)
        else:
            vals[vals.index(max(vals))] += J_count
    
    vals.sort()

    if vals[0] == 5:
        rank[7].append((hand[0], hand[1]))
    elif vals == [2, 3]:
        rank[5].append((hand[0], hand[1]))
    elif vals == [1, 1, 1, 1, 1]:
        rank[1].append((hand[0], hand[1]))
    elif vals == [1, 1, 1, 2]:
        rank[2].append((hand[0], hand[1]))
    elif vals == [1, 1, 3]:
        rank[4].append((hand[0], hand[1]))
    elif vals == [1, 2, 2]:
        rank[3].append((hand[0], hand[1]))
    elif vals == [1, 4]:
        rank[6].append((hand[0], hand[1]))
        
total = 0
curr = 0

def compareHands(a, b):
    for j in range(0, 5):
        diff = cards.index(a[0][j]) - cards.index(b[0][j])
        if diff != 0:
            return -diff

for i in rank.keys():
    if len(rank[i]) == 1:
        curr += 1
        total += curr * int(rank[i][0][1])
    elif len(rank[i]) > 1:
        sorted_hands = sorted(rank[i], key=cmp_to_key(compareHands))
        for j in sorted_hands:
            curr += 1
            total += curr * int(j[1])

print(total)