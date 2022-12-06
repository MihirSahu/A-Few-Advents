# Helper function
def check_duplicate(stack):
    for char in stack:
        if stack.count(char) > 1:
            return True
    return False

# Main code
stack = []

with open("input", 'r') as file:
    for line in file:
        for idx in range(0, 13):
            stack.append(line[idx])
        for idx in range(13, len(line)):
            print(stack, line[idx])
            if (line[idx] not in stack) and (check_duplicate(stack) == False):
                print(idx + 1)
                break
            else:
                stack.pop(0)
                stack.append(line[idx])