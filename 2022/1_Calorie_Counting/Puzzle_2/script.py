calories = []
first_max = 0
second_max = 0
third_max = 0

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
    if calorie > first_max:
        third_max = second_max
        second_max = first_max
        first_max = calorie
    elif calorie > second_max and calorie != first_max:
        third_max = second_max
        second_max = calorie
    elif calorie > third_max and calorie != second_max:
        third_max = calorie

print(first_max + second_max + third_max)
