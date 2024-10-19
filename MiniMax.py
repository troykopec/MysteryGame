import random
from GameRules import *


# AI name
def name():
    return 'LookAheadAI'

# Recursive function to generate the tree and count nodes
def lookAhead(state, depth=1):
    if depth == 0 or isGameOver(state):
        return state, 1

    legal_moves = getAllLegalMoves(state)
    total_nodes = 1  # Current state is one node

    best_move = None
    best_state = None
    max_captures = -1

    for move in legal_moves:
        new_state = playMove(state, move)
        if new_state is None:
            continue
        
        # Recursively look ahead
        _, nodes = lookAhead(new_state, depth - 1)
        total_nodes += nodes

        # Evaluate based on captures
        captures = new_state['LightCapture'] if new_state['Turn'] == 'Dark' else new_state['DarkCapture']

        if captures > max_captures:
            max_captures = captures
            best_move = move
            best_state = new_state

    return best_state, total_nodes

# AI function to select the best move
def getMove(state):
    # Look ahead by one move (depth=1)
    best_state, total_nodes = lookAhead(state, depth=3)

    # Print the total number of nodes in the tree
    print(f"Total nodes in the move tree: {total_nodes}")

    if best_state:
        legal_moves = getAllLegalMoves(state)
        for move in legal_moves:
            # Compare the state after each legal move and return the matching one
            if playMove(state, move) == best_state:
                print(f"LOOK AHEAD AI TAKING: {move['Direction']}")
                return move

    # Fallback to random move if no best move found
    legal_moves = getAllLegalMoves(state)
    move = random.choice(legal_moves)
    print(f"LOOK AHEAD AI TAKING: {move['Direction']}")
    return move
