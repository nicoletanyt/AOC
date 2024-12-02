with open('input.txt') as f:
    lines = [line.rstrip().split() for line in f]

count = 0

for report in lines:
    safe = True
    direction = -1 # 0 is increasing, 1 is decreasing

    for level in range(1, len(report)):
        # if same, not safe
        diff = abs(int(report[level]) - int(report[level - 1]))
        if diff >= 1 and diff <= 3:
            if int(report[level]) > int(report[level - 1]):
                # increasing 
                if direction == 1:
                    # different direction
                    safe = False
                    break
                direction = 0
            else: 
                # decreasing
                if direction == 0:
                    # different direction
                    safe = False
                    break
                direction = 1
        else: 
            # difference is > 3 or < 1
            safe = False
            break

    if (safe):
        count += 1
    
print(count)

# MORE READABLE SOLUTION:

# with open('input.txt') as f:
#     lines = [[int(j) for j in line.rstrip().split()] for line in f]

# count = 0

# for report in lines:
#     # make copies and sort the reports
#     inc = report.copy()
#     inc.sort()
#     dec = report.copy()
#     dec.sort(reverse=True)

#     same_direction = False # 1: all are increasing, 0: all are decreasing
#     safe = True

#     # check if all are either increasing/decreasing
#     if report == inc or report == dec:
#         same_direction = True

#     if same_direction:
#         for level in range(1, len(report)):
#             # if same, not safe
#             diff = abs(int(report[level]) - int(report[level - 1]))

#             if  diff < 1 or diff > 3:
#                 safe = False
#                 break

#         if (safe):
#             count += 1
    
# print(count)