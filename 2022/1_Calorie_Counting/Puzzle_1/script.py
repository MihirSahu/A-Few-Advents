calories = []
maximum_calories = 0

with open("input", "r") as file:

    for line in file:
        if line.rstrip() == "" and len(calories) != 0:
            calories.append(0)
            continue
        elif len(calories) != 0:
            calories[-1] = calories[-1] + int(line.rstrip())
        else:
            calories.append(int(line.rstrip()))

for calorie in calories:
    if calorie > maximum_calories:
        maximum_calories = calorie

print(maximum_calories)
