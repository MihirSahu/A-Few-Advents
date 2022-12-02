opponent_moves = {'A': 1, 'B': 2, 'C': 3}
your_moves = {'X': 1, 'Y': 2, 'Z': 3}
outcomes = {'X': 0, 'Y': 3, 'Z': 6}
total_score = 0

with open("input", 'r') as file:
    for line in file:
        moves = line.rstrip().split()

        if moves[0] == 'A' and moves[1] == 'X':
            total_score = total_score + your_moves[list(your_moves.keys())[2]] + outcomes[moves[1]]
        elif moves[0] == 'A' and moves[1] == 'Y':
            total_score = total_score + your_moves[list(your_moves.keys())[0]] + outcomes[moves[1]]
        elif moves[0] == 'A' and moves[1] == 'Z':
            total_score = total_score + your_moves[list(your_moves.keys())[1]] + outcomes[moves[1]]
        elif moves[0] == 'B' and moves[1] == 'X':
            total_score = total_score + your_moves[list(your_moves.keys())[0]] + outcomes[moves[1]]
        elif moves[0] == 'B' and moves[1] == 'Y':
            total_score = total_score + your_moves[list(your_moves.keys())[1]] + outcomes[moves[1]]
        elif moves[0] == 'B' and moves[1] == 'Z':
            total_score = total_score + your_moves[list(your_moves.keys())[2]] + outcomes[moves[1]]
        elif moves[0] == 'C' and moves[1] == 'X':
            total_score = total_score + your_moves[list(your_moves.keys())[1]] + outcomes[moves[1]]
        elif moves[0] == 'C' and moves[1] == 'Y':
            total_score = total_score + your_moves[list(your_moves.keys())[2]] + outcomes[moves[1]]
        elif moves[0] == 'C' and moves[1] == 'Z':
            total_score = total_score + your_moves[list(your_moves.keys())[0]] + outcomes[moves[1]]

print(total_score)
