# Part 1
'''
lhs = []
rhs = []
sum = 0

with open("./inputs/1-Historian-Hysteria.txt") as file:
  for line in file:
    split_line = line.rstrip().split()
    lhs.append(int(split_line[0]))
    rhs.append(int(split_line[1]))
    lhs = sorted(lhs)
    rhs = sorted(rhs)

for idx in range(len(lhs)):
  sum += abs(lhs[idx] - rhs[idx])

print(sum)
'''

lhs = []
rhs = []
similarity_map = {}
similarity_score = 0

with open("./inputs/1-Historian-Hysteria.txt") as file:
  for line in file:
    split_line = line.rstrip().split()
    lhs.append(split_line[0])
    rhs.append(split_line[1])

for idx in range(len(rhs)):
  if rhs[idx] in similarity_map:
    similarity_map[rhs[idx]] += 1
  else:
    similarity_map[rhs[idx]] = 1

for idx in range(len(lhs)):
  similarity_score += int(lhs[idx]) * int(similarity_map.get(lhs[idx], 0))

print(similarity_score)