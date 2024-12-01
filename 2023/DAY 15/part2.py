with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

seq = lines[0].split(",")
total = 0
box = {} # box number : [[label, focus no.], []]

def hash_num(i):
    val = 0
    for j in i:
        val += ord(j)
        val *= 17
        val = val % 256
    return val 

for i in seq:
    label = ""
    for j in range(0, len(i)):
        if i[j] == "=":
            # add new box 
            if hash_num(label) in box:
                exist = False
                for k in range(0, len(box[hash_num(label)])):
                    if box[hash_num(label)][k][0] == label:
                       box[hash_num(label)][k][1] =  int(i[j + 1:])
                       exist = True 
                if not exist:
                    box[hash_num(label)].append([label, int(i[j + 1:])])
            else:
                box[hash_num(label)] = [[label, int(i[j + 1:])]]
        elif i[j] == "-":
            # check for another with the same label, if yes, remove 
            for k in box:
                if box[k]:
                    for l in range(0, len(box[k])):
                        if box[k][l][0] == label:
                            box[k].remove(box[k][l])
                            break

            [[k.remove(k[l]) for l in range(0, len(k)) if k[l][0] == label] for k in box.values()]
        else:
            label += i[j]

for i in box:
    for j in range(0, len(box[i])):
        num = (i + 1) * (j + 1) * box[i][j][1]
        total += num 
    
print(total)