count = 0

with open('input', 'r') as file:
    for line in file:
        range_pair = line.rstrip().split(',')

        for idx in range(0, len(range_pair)):
            range_pair[idx] = range(int(range_pair[idx].split('-')[0]), int(range_pair[idx].split('-')[1]) + 1)

        if set(range_pair[0]).issubset(range_pair[1]) or set(range_pair[1]).issubset(range_pair[0]):
            count += 1

print(count)
