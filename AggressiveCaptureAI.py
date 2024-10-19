import random
from GameRules import *

# AI name
def name():
    return 'AggressiveCaptureAI'

# AI function to select the best move
def getMove(state):
    player_color = state['Turn']
    legal_moves = getAllLegalMoves(state)
    if not legal_moves:
        return None

    best_moves = []
    max_capture = -1

    for move in legal_moves:
        new_state = playMove(state, move)
        if new_state is None:
            continue

        # Calculate the number of pieces captured
        player_captured = new_state['LightCapture'] if player_color == 'Light' else new_state['DarkCapture']
        prev_player_captured = state['LightCapture'] if player_color == 'Light' else state['DarkCapture']
        captures = player_captured - prev_player_captured

        if captures > max_capture:
            max_capture = captures
            best_moves = [move]
        elif captures == max_capture:
            best_moves.append(move)

    if best_moves:
        move = random.choice(best_moves)
        print(f"AGGRESSIVE CAPTURE AI SELECTED MOVE: {move}")
        return move
    else:
        # If no captures are possible, pick a random legal move
        move = random.choice(legal_moves)
        print(f"AGGRESSIVE CAPTURE AI SELECTED RANDOM MOVE: {move}")
        return move
