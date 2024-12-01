data = open("input.txt", "r")
lines = data.read().split()
left_list = []
right_list = {}
total = 0

# read data
data = open("data.txt", "r")
lines = data.read().split()
for i in range(0, len(lines)):
    if i % 2 == 0:
        # left list 
        left_list.append(int(lines[i]))
    else:
        # add right list elements to a map 
        if int(lines[i]) in right_list: 
            right_list[int(lines[i])] += 1
        else: 
            right_list[int(lines[i])] = 1

# multiply
for i in range(0, len(left_list)):
    if left_list[i] in right_list:
        total += (left_list[i] * right_list[left_list[i]])

print(total)
