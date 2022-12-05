# Helper functions

# https://www.geeksforgeeks.org/python-transpose-elements-of-two-dimensional-list/
def transpose(l1, l2):

	# iterate over list l1 to the length of an item
	for i in range(len(l1[0])):
		# print(i)
		row =[]
		for item in l1:
			# appending to new list with values and index positions
			# i contains index position and item contains values
			row.append(item[i])
		l2.append(row)
	return l2

def parse_instruction(line):
    instruction = line.split()
    return [int(instruction[1]), int(instruction[3]), int(instruction[5])]

def print_stacks(stacks):
    greatest_length = 0
    for stack in stacks:
        if len(stack) > greatest_length:
            greatest_length = len(stack)
    for idx in range(greatest_length, 0 , -1):
        for stack in stacks:
            if idx > len(stack):
                print("   ", end="")
            else:
                print(f" {stack[len(stack) - idx]} ", end="")
        print()


# Main code
stacks = []
num_stacks = 0

with open("input", 'r') as file:

    # Find the number of stacks
    for line in file:
        if line[0:2] == " 1":
            num_stacks = int(line.rstrip()[-1])
            break

with open("input", 'r') as file:

    for line in file:
        if line[0:2] == " 1":
            break
        temp = [''] * num_stacks

        # Parse the rows
        line_counter = 1
        list_counter = 0
        while line_counter < len(line):
            temp[list_counter] = line[line_counter]
            line_counter = line_counter + 4
            list_counter = list_counter + 1
        stacks.append(temp)

stacks = transpose(stacks, [])

for stack in stacks:
    while stack[0] == ' ':
        stack.pop(0)

with open("input", 'r') as file:

    for line in file:
        if line[0:2] == " 1":
            break
    next(file)
    for line in file:
        instruction = parse_instruction(line)
        if instruction[0] <= 1:
            if stacks[instruction[1] - 1] == []:
                break
            for i in range(0, instruction[0]):
                stacks[instruction[2] - 1].insert(0, stacks[instruction[1] - 1].pop(0))
        elif instruction[0] > 1:
            if instruction[0] >= len(stacks[instruction[1] - 1]):
                stacks[instruction[2] - 1][:0] = stacks[instruction[1] - 1][0:]
                del stacks[instruction[1] - 1][0:]
            else:
                stacks[instruction[2] - 1][:0] = stacks[instruction[1] - 1][0:instruction[0]]
                del stacks[instruction[1] - 1][0:instruction[0]]

print_stacks(stacks)
for stack in stacks:
    if stack == []:
        print(" ", end="")
    else:
        print(stack[0], end="")