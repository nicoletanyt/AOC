with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

stones = lines[0].split()

for _ in range(25):
    n = len(stones)
    i = 0
    while i < n:
        current = stones[i]
        if stones[i] == "0":
            stones[i] = "1"
        
        elif len(stones[i]) % 2 == 0:
            # even digits, split stone
            n += 1
            stones[i] = current[:len(current) // 2]
            # typecast to remove leading 0
            stones.insert(i + 1, str(int(current[len(current) // 2:])))
            i += 1
        
        else:
            # multiply by 2024
            stones[i] = str(int(stones[i]) * 2024)

        i += 1

print(len(stones))