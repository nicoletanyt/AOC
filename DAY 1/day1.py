sum = 0

with open('DAY 1/input.txt') as f:
    lines = [line.rstrip() for line in f]

nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for i in lines:
    num = ""
    temp = ""
    for j in range(0, len(i)):
        if i[j].isdigit():
            num += i[j]
            break
        else:
            temp += i[j]
            for k in list(nums.keys()):
                if k in temp:
                    num += nums[k]
                    i = i.replace(k, nums[k])
                    break
            if len(num) == 1:
                break

    temp = ""
    for j in range(len(i) - 1, -1, -1):
        if i[j].isdigit():
            num += i[j]
            break
        else:
            temp = i[j] + temp
            for k in list(nums.keys()):
                if k in temp:
                    num += nums[k]
                    break
            if len(num) == 2:
                break

    sum += int(num)

print(sum)