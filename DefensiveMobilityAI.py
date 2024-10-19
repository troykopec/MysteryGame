import random
from GameRules import *

# AI name
def name():
    return 'DefensiveMobilityAI'

def eval_mobility(state, player_color):
    # Evaluate the mobility for both players
    player_moves = len(getAllLegalMoves(state))
    opponent_state = copyState(state)
    opponent_state['Turn'] = 'Dark' if player_color == 'Light' else 'Light'
    opponent_moves = len(getAllLegalMoves(opponent_state))

    # Mobility difference
    mobility_score = player_moves - opponent_moves
    return mobility_score

# AI function to select the best move
def getMove(state):
    player_color = state['Turn']
    legal_moves = getAllLegalMoves(state)
    if not legal_moves:
        return None

    best_moves = []
    max_mobility = float('-inf')

    for move in legal_moves:
        new_state = playMove(state, move)
        if new_state is None:
            continue

        # Evaluate mobility after the move
        mobility_score = eval_mobility(new_state, player_color)

        if mobility_score > max_mobility:
            max_mobility = mobility_score
            best_moves = [move]
        elif mobility_score == max_mobility:
            best_moves.append(move)

    if best_moves:
        move = random.choice(best_moves)
        print(f"DEFENSIVE MOBILITY AI SELECTED MOVE: {move}")
        return move
    else:
        # Fallback to random move
        move = random.choice(legal_moves)
        print(f"DEFENSIVE MOBILITY AI SELECTED RANDOM MOVE: {move}")
        return move
