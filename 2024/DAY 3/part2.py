with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def returnProduct(index: int, current_string: str):
    first_num = ""
    second_num = ""
    before_comma = True
    # skip to the first character after mul(
    for i in range(index + 4, len(current_string)):
        if current_string[i].isdigit():
            if before_comma:
                first_num += current_string[i]
            else:
                second_num += current_string[i]
        elif current_string[i] == ",":
            if not before_comma: 
                return (-1, i + 1)
            before_comma = False
        elif current_string[i] == ")":
            if first_num != "" and second_num != "":
                # return the (product, stopIndex) as both numbers are valid
                return (int(first_num) * int(second_num), i + 1)
        else:
            # any other invalid character
            return (-1, i + 1)

def returnInstructions(current_string: str):
    while True:
        dont_index = current_string.find("don't()")
        if dont_index == -1:
            return current_string
        else:
            # find the next do_index to see if it ever gets enabled again
            string_copy = current_string[dont_index + 8:] # start looping 7 characters (don't()) after
            do_index = string_copy.find("do()")
            if do_index == -1:
                # rest of the string doesn't matter
                return current_string[:dont_index]
            else:
                # remove the part between dont() and do()
                current_string = current_string[:dont_index] + current_string[dont_index + 7 + do_index + 5:] # exclude the 4 do() characters
    

valid = False
total = 0

# filter the parts in between don't and do that is invalid
current_string = returnInstructions("".join(lines))
index = current_string.find("mul(")

while True:
    product, stopIndex = returnProduct(index, current_string)

    # remove the characters that had been looped through
    current_string = current_string[stopIndex:]
    if product != -1: 
        total += product
    index = current_string.find("mul(")

    if index == -1:
        break

print(total)