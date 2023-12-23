with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

workflows = {}
total = 0

for i in lines:
    if i != "":
        if i[0] == "{":
            curr_w = "in"
            val = {}
            parts = i[1:-1].split(",")
            for j in parts:
                val[j[0]] = j[2:] # xmas values 

            while curr_w != "R" and curr_w != "A":
                done = False 
                for j in range(0, len(workflows[curr_w]) - 1):
                    v = int(val[workflows[curr_w][j][0]])
                    colon = workflows[curr_w][j].index(":")
                    if workflows[curr_w][j][1] == "<":
                        if v < int(workflows[curr_w][j][2:colon]):
                            # next workflow 
                            curr_w = workflows[curr_w][j][colon + 1:]
                            done = True 
                            break
                    elif workflows[curr_w][j][1] == ">":
                        if v > int(workflows[curr_w][j][2:colon]):
                            # next workflow 
                            curr_w = workflows[curr_w][j][colon + 1:]
                            done = True 
                            break
                if not done:
                    # set to default 
                    curr_w = workflows[curr_w][-1][:-1]
            if curr_w == "A":
                # print(val.values())
                total += sum([int(x) for x in list(val.values())])

        else:
            part = i.split("{")
            rules = part[1].split(",")
            workflows[part[0]] = rules

print(total)

# print(workflows)