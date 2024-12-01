with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

workflows = {}

# parse input 
for i in lines:
    if i != "" and i[0] != "{":
        part = i[:-1].split("{")
        rules = part[1].split(",")
        workflows[part[0]] = (rules[:-1], rules[-1])

def count(r, name = "in"):
    total = 0

    if name == "R": return 0 # don't count 
    if name == "A": 
        product = 1
        for l, h in r.values():
            product *= h - l + 1
        return product
    
    rules, default = workflows[name]
    for i in rules:
        condition, target = i.split(":")
        l, h = r[condition[0]]
        if condition[1] == ">":
            cmp_index = condition.index(">")
            if int(condition[cmp_index + 1:]) + 1 <= h: 
                # condition is true, set to target workflow. lower bound should change  
                copy = dict(r)
                copy[condition[0]] = (int(condition[cmp_index + 1:]) + 1, h)
                total += count(copy, target)
            if l <= int(condition[cmp_index + 1:]):
                r = dict(r)
                r[condition[0]] = (l, int(condition[cmp_index + 1:]))
            else:
                break
        else:
            cmp_index = condition.index("<")
            if l <= int(condition[cmp_index + 1:]) - 1: 
                # condition is true, set to target workflow. upper bound should change 
                copy = dict(r)
                copy[condition[0]] = (l, int(condition[cmp_index + 1:]) - 1)
                total += count(copy, target)
            if int(condition[cmp_index + 1:]) <= h:
                r = dict(r)
                r[condition[0]] = (int(condition[cmp_index + 1:]), h)
            else:
                break
    else:
        total += count(r, default)

    return total

print(count({key: (1, 4000) for key in "xmas"})) # inclusive range