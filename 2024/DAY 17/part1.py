import math
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

# parse the data 
A = int(lines[0].split(": ")[1])
B = int(lines[1].split(": ")[1])
C = int(lines[2].split(": ")[1])
program = lines[4].split(": ")[1].split(",")

instruction_pointer = 0
output = []

def return_combo(operand):
    if operand >= 0 and operand <= 3:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    return C

while instruction_pointer + 1 < len(program):
    opcode = int(program[instruction_pointer])
    operand = int(program[instruction_pointer + 1])

    instruction_pointer += 2
    # handle instruction 
    if opcode == 0:
        A = math.trunc(A / (2 ** return_combo(operand)))
    elif opcode == 1:
        B = B ^ operand
    elif opcode == 2:
        B = return_combo(operand) % 8
    elif opcode == 3 and A != 0:
        # jumps by setting instruction pointer to literal operand
        instruction_pointer = operand
        # note: does not jump
    elif opcode == 4:
        B = B ^ C
    elif opcode == 5:
        output.append(return_combo(operand) % 8)
    elif opcode == 6:
        B = math.trunc(A / (2 ** return_combo(operand)))
    else:
        C = math.trunc(A / (2 ** return_combo(operand)))

# output
output = [str(i) for i in output]
if len(output) > 0:
    print(",".join(output))
else:
    print("No output")
    

