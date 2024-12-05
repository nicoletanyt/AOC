with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

# parse the data
section_sep = lines.index("")
first_section = lines[:section_sep]
second_section = lines[section_sep + 1:]

numbers = {} # stores the numbers and whichever numbers have to be in front of them
total = 0

def checkValid(num: list[str]):
    prev = []
    for i in num:
        # for this to be valid, there should not be any common numbers between numbers[i] and prev 
        for j in prev:
            if i in numbers and j in numbers[i]:
                # invalid 
                return False

        prev.append(i)
    
    return True

for pair in first_section:
    first_num, second_num = pair.split("|")
    if second_num in numbers:
        numbers[second_num].append(first_num)
    else:
        numbers[second_num] = [first_num]

for line in second_section:
    num = line.split(",")
    # reverse the line
    num.reverse()
    if checkValid(num):
        # add the middle number
        total += int(num[len(num) // 2])

print(total)


