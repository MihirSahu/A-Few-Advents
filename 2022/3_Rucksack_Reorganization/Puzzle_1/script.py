import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
total_priority = 0

with open("input", 'r') as file:
    for line in file:
        items = line.rstrip()
        first_compartment = list(items[0:int(len(items)/2)])
        second_compartment = list(items[int(len(items)/2):])

        common_item = list(set(first_compartment).intersection(second_compartment))[0]

        if common_item in lowercase:
            total_priority = total_priority + lowercase.index(common_item) + 1
        elif common_item in uppercase:
            total_priority = total_priority + uppercase.index(common_item) + 27

print(total_priority)
