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
print(stacks)

with open("input", 'r') as file:

    for line in file:
        if line[0:2] == " 1":
            break
    next(file)
    for line in file:
        instruction = parse_instruction(line)
        #for i in range(0, instruction[0]):
        #    stacks[instruction[1] + 1]
        #    stacks[instruction[2] + 1]