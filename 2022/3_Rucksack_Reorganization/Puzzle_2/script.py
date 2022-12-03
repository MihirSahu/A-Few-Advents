import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
total_priority = 0
line_counter = 0
items = []

with open("input", 'r') as file:
    for line in file:

        if line_counter < 2:
            line_counter += 1
            items.append(line.rstrip())

        elif line_counter == 2:
            items.append(line.rstrip())
            common_item = list(set(list(items[0])).intersection(list(items[1])))
            common_item = list(set(common_item).intersection(list(items[2])))[0]

            if common_item in lowercase:
                total_priority = total_priority + lowercase.index(common_item) + 1
            elif common_item in uppercase:
                total_priority = total_priority + uppercase.index(common_item) + 27

            items.clear()
            line_counter = 0

print(total_priority)
