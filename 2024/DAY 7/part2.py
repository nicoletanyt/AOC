with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0

for l in lines:
    # parse the data
    result, n = l.split(": ")
    numbers = [int(i) for i in n.split(" ")]
    result = int(result)
    n = len(numbers)

    def recur(current: int, index: int):
        # return True if this is the last element 
        if current == result and index == n: return True
        if current > result or index >= n: return False
        
        # otherwise, multiply, add it again, or concatenate
        return recur(current * numbers[index], index + 1) or recur(current + numbers[index], index + 1) or recur(int(str(current) + str(numbers[index])), index + 1)

    if recur(1, 0):
        total += result

print(total)
