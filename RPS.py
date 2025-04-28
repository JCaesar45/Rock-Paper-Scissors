import random

def player(prev_play, opponent_history=[]):
    # If it's the first turn, choose randomly
    if prev_play == "":
        return random.choice(["R", "P", "S"])

    # Record the opponent's last move
    opponent_history.append(prev_play)

    # Move counter for the opponent's moves
    move_counter = {
        "R": 0,
        "P": 0,
        "S": 0
    }

    # Count the opponent's moves
    for move in opponent_history:
        move_counter[move] += 1

    # Determine the most common opponent's move
    most_common_move = max(move_counter, key=move_counter.get)

    # Choose the winning move against the most common opponent's move
    if most_common_move == "R":
        return "P"  # Paper beats Rock
    elif most_common_move == "P":
        return "S"  # Scissors beat Paper
    elif most_common_move == "S":
        return "R"  # Rock beats Scissors

    # In case of a tie or unexpected input, return a random choice
    return random.choice(["R", "P", "S"])
