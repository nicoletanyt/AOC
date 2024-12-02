with open('input.txt') as f:
    lines = [[int(j) for j in line.rstrip().split()] for line in f]

count = 0

def returnError(report):
    direction = -1 # 0 is increasing, 1 is decreasing

    for level in range(0, len(report) - 1):
        # if same, not safe
        diff = abs(report[level + 1] - report[level])
        if diff >= 1 and diff <= 3:
            if report[level + 1] > report[level]:
                # increasing 
                if direction == 1:
                    # different direction
                    return level
                direction = 0
            else: 
                # decreasing
                if direction == 0:
                    # different direction
                    return level
                direction = 1
        else: 
            # difference is > 3 or < 1
            return level
    
    return -1
    
# BRUTE FORCE

for report in lines:
    error = returnError(report)
    if error == -1:
        # no error in report
        count += 1
    else:
        # trying removing each of the numbers and try again
        for i in range(0, len(report)):
            new_report = report.copy()
            del new_report[i]
            if returnError(new_report) == -1:
                count += 1
                # print(report)
                break

print(count)
    