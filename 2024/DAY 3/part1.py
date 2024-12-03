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

valid = False
current_string = "".join(lines) 
index = current_string.find("mul(")
total = 0

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