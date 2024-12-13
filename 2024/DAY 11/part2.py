with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

stones = lines[0].split()

total = 0
cache = {}

# recursion method + memo

def recursion(stone, count):
    # base case 
    if count == 75:
        return 1
    
    if stone in cache:
        if count in cache[stone]:
            return cache[stone][count]

    if stone == "0":
        answer = recursion("1", count + 1)
    elif len(stone) % 2 == 0:
        # even digits, split stone
        # typecast to remove leading 0
        answer = recursion(stone[:len(stone) // 2], count + 1) + recursion(str(int(stone[len(stone) // 2:])), count + 1)
    else:
        answer = recursion(str(int(stone) * 2024), count + 1)
    
    if stone in cache:
        cache[stone][count] = answer
    else:
        cache[stone] = {count: answer}
    
    return answer

for i in stones:
    total += recursion(i, 0)

print(total)