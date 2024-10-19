import random
from GameRules import *

# AI name
def name():
    return 'StackBuilderAI'

def is_diagonal_move(move):
    return move['Direction'] in ['NE', 'NW', 'SE', 'SW']

# AI function to select the best move
def getMove(state):
    legal_moves = getAllLegalMoves(state)
    if not legal_moves:
        return None

    # Prioritize diagonal moves that combine stacks
    diagonal_moves = []
    for move in legal_moves:
        if is_diagonal_move(move):
            diagonal_moves.append(move)

    if diagonal_moves:
        # Choose the move that results in the largest stack
        max_stack = -1
        best_moves = []
        for move in diagonal_moves:
            new_state = playMove(state, move)
            if new_state is None:
                continue

            target_row, target_col = get_target_square(state['Board'], move)
            if target_row is not None:
                stack_size = getPieces(new_state['Board'], target_row, target_col)
                if stack_size > max_stack:
                    max_stack = stack_size
                    best_moves = [move]
                elif stack_size == max_stack:
                    best_moves.append(move)

        if best_moves:
            move = random.choice(best_moves)
            print(f"STACK BUILDER AI SELECTED MOVE: {move}")
            return move

    # If no diagonal moves, pick any move
    move = random.choice(legal_moves)
    print(f"STACK BUILDER AI SELECTED RANDOM MOVE: {move}")
    return move

def get_target_square(board, move):
    row = move['Row']
    col = move['Col']
    direction = move['Direction']

    if direction == 'NE':
        delta_row, delta_col = -1, 1
    elif direction == 'NW':
        delta_row, delta_col = -1, -1
    elif direction == 'SE':
        delta_row, delta_col = 1, 1
    elif direction == 'SW':
        delta_row, delta_col = 1, -1
    else:
        return None, None

    new_row = row
    new_col = col
    while True:
        new_row += delta_row
        new_col += delta_col
        if new_row < 0 or new_row > 5 or new_col < 0 or new_col > 5:
            return None, None
        if getPieces(board, new_row, new_col) != 0:
            return new_row, new_col
