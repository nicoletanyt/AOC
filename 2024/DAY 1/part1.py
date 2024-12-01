left_list = []
right_list = []
total = 0

# read data
data = open("input.txt", "r")
lines = data.read().split()
for i in range(0, len(lines)):
    if i % 2 == 0:
        # left list 
        left_list.append(int(lines[i]))
    else:
        right_list.append(int(lines[i]))

# sort lists 
left_list.sort()
right_list.sort()

for i in range(0, len(left_list)):
    total += (abs(right_list[i] - left_list[i]))

print(total)

