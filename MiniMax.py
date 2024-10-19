import random
from GameRules import *

# AI name
def name():
    return 'EnhancedMinimaxAI'

# evaluation function
def eval(state, player_color):
    opponent_color = 'Dark' if player_color == 'Light' else 'Light'

    # total number of pieces on the board
    player_pieces = 0
    opponent_pieces = 0

    # number of pieces in the middle of the board
    player_middle_pieces = 0
    opponent_middle_pieces = 0

    middle_rows = [2, 3]
    middle_cols = [2, 3]

    for i in range(6):
        for j in range(6):
            pieces = getPieces(state['Board'], i, j)
            square_color = color(i, j)
            if square_color == player_color:
                player_pieces += pieces
                if i in middle_rows and j in middle_cols:
                    player_middle_pieces += pieces
            else:
                opponent_pieces += pieces
                if i in middle_rows and j in middle_cols:
                    opponent_middle_pieces += pieces

    player_captured = state['LightCapture'] if player_color == 'Light' else state['DarkCapture']
    opponent_captured = state['LightCapture'] if opponent_color == 'Light' else state['DarkCapture']

    # check if it's early game or not
    total_captured_pieces = player_captured + opponent_captured

    if total_captured_pieces < 10:
        # early game, prioritize middle control
        eval_value = (
            (player_pieces + player_captured)
            - (opponent_pieces + opponent_captured)
            + 2 * (player_middle_pieces - opponent_middle_pieces)
        )
    else:
        # later game, prioritize total pieces and captures
        eval_value = (
            (player_pieces + 2 * player_captured)
            - (opponent_pieces + 2 * opponent_captured)
        )

    return eval_value

# MiniMax function with alpha-beta pruning
def minimax(state, depth, alpha, beta, maximizingPlayer, player_color):
    if depth == 0 or isGameOver(state):
        return eval(state, player_color), None

    legal_moves = getAllLegalMoves(state)
    if not legal_moves:
        # no legal moves, game over
        return eval(state, player_color), None

    if maximizingPlayer:
        maxEval = float('-inf')
        best_move = None
        for move in legal_moves:
            new_state = playMove(state, move)
            if new_state is None:
                continue
            eval_value, _ = minimax(new_state, depth - 1, alpha, beta, False, player_color)
            if eval_value > maxEval:
                maxEval = eval_value
                best_move = move
            alpha = max(alpha, eval_value)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in legal_moves:
            new_state = playMove(state, move)
            if new_state is None:
                continue
            eval_value, _ = minimax(new_state, depth - 1, alpha, beta, True, player_color)
            if eval_value < minEval:
                minEval = eval_value
                best_move = move
            beta = min(beta, eval_value)
            if beta <= alpha:
                break
        return minEval, best_move

# AI function to select the best move
def getMove(state):
    player_color = state['Turn']
    opponent_color = 'Dark' if player_color == 'Light' else 'Light'

    # depth for the minimax algorithm
    depth = 3  # Adjust the depth as needed for performance

    # Call minimax to get the best move
    eval_value, best_move = minimax(state, depth, float('-inf'), float('inf'), True, player_color)

    if best_move:
        print(f"MINIMAX AI SELECTED MOVE: {best_move}")
        return best_move

    # Fallback to random move if no best move found
    legal_moves = getAllLegalMoves(state)
    move = random.choice(legal_moves)
    print(f"MINIMAX AI SELECTED RANDOM MOVE: {move}")
    return move
