import math

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

ranges = lines[0].split(",")
total = 0

for r in ranges:
    first, second = r.split("-")
    first, second = int(first), int(second)

    for i in range(first, second + 1):
        id = str(i)
        length = len(id)
        diff = []

        # get all differences
        for j in range(1, length):
            diff.append(int(id[j]) - int(id[j - 1]))

        intervals = []
        curr_sum = 0
        try_len = -1
        for j in range(0, len(diff)):
            curr_sum += diff[j]
            if curr_sum == 0:
                intervals.append(j)
                if len(intervals) == 2:
                    try_len = intervals[1] - intervals[0]
                    break

        if try_len != -1 and id[:try_len] * int(length / try_len) == id:
            # print(id)
            total += i
        elif length % 2 == 0 and id[: math.floor(length / 2)] == id[int(length / 2) :]:
            # print(id)
            total += i

print(total)
