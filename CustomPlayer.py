import random
from GameRules import *
import time

# AI name
def name():
    return 'StrategicMinimaxAI'

# Parameters to optimize
EVAL_WEIGHTS = {
    'pieces': 1.0,
    'captured': 1.0,
    'middle_pieces': 3.0,
    'largest_stack_penalty': 0.2,
    'potential_captures': 1.0,
    'mobility': 1.0,
    'largest_stack_bonus': 1.0,
}

DEPTHS = {
    'early': 3,
    'mid': 3,
    'late': 6,
}

TIME_LIMITS = {
    'early': 5,  # seconds
    'mid': 10,   # seconds
    'late': 15,  # seconds
}

GAME_STAGE_THRESHOLDS = {
    'early_captured_pieces': 10,
    'mid_captured_pieces': 30,
    'average_stack_size': 1.5,
    'large_stacks': 3,
}

# Function to set parameters from outside
def set_parameters(eval_weights=None, depths=None, time_limits=None, thresholds=None):
    global EVAL_WEIGHTS, DEPTHS, TIME_LIMITS, GAME_STAGE_THRESHOLDS
    if eval_weights is not None:
        EVAL_WEIGHTS.update(eval_weights)
    if depths is not None:
        DEPTHS.update(depths)
    if time_limits is not None:
        TIME_LIMITS.update(time_limits)
    if thresholds is not None:
        GAME_STAGE_THRESHOLDS.update(thresholds)

# Evaluation function
def eval(state, player_color, game_stage):
    opponent_color = 'Dark' if player_color == 'Light' else 'Light'

    # Total number of pieces on the board for each player
    player_pieces = 0
    opponent_pieces = 0

    # Number of pieces in the middle of the board
    player_middle_pieces = 0
    opponent_middle_pieces = 0

    # Mobility: number of legal moves
    player_mobility = len(getAllLegalMoves(state)) if state['Turn'] == player_color else 0
    opponent_state = copyState(state)
    opponent_state['Turn'] = opponent_color
    opponent_mobility = len(getAllLegalMoves(opponent_state))

    middle_rows = [2, 3]
    middle_cols = [2, 3]

    # Largest stack sizes
    player_largest_stack = 0
    opponent_largest_stack = 0

    for i in range(6):
        for j in range(6):
            pieces = getPieces(state['Board'], i, j)
            square_color = color(i, j)
            if square_color == player_color:
                player_pieces += pieces
                if pieces > player_largest_stack:
                    player_largest_stack = pieces
                if i in middle_rows and j in middle_cols:
                    player_middle_pieces += pieces
            else:
                opponent_pieces += pieces
                if pieces > opponent_largest_stack:
                    opponent_largest_stack = pieces
                if i in middle_rows and j in middle_cols:
                    opponent_middle_pieces += pieces

    player_captured = state['LightCapture'] if player_color == 'Light' else state['DarkCapture']
    opponent_captured = state['LightCapture'] if opponent_color == 'Light' else state['DarkCapture']

    # Use weights from EVAL_WEIGHTS
    weights = EVAL_WEIGHTS

    # Evaluation based on game stage
    if game_stage == 'early':
        # Early game: prioritize middle control and reasonable stack sizes
        eval_value = (
            weights['pieces'] * (player_pieces + player_captured - opponent_pieces - opponent_captured)
            + weights['middle_pieces'] * (player_middle_pieces - opponent_middle_pieces)
            - weights['largest_stack_penalty'] * max(0, player_largest_stack - 3)
            + weights['potential_captures'] * potential_capture_score(state, player_color)
        )
    elif game_stage == 'mid':
        # Mid game: prioritize captures and mobility
        eval_value = (
            weights['pieces'] * (player_pieces + 2 * player_captured - opponent_pieces - 2 * opponent_captured)
            + weights['mobility'] * (player_mobility - opponent_mobility)
        )
    else:
        # Late game: maximize number of moves and prepare for endgame bonus
        eval_value = (
            weights['pieces'] * (player_pieces + 3 * player_captured - opponent_pieces - 3 * opponent_captured)
            + weights['mobility'] * (player_mobility - opponent_mobility) * 2
            + weights['largest_stack_bonus'] * player_largest_stack
        )

    return eval_value

def potential_capture_score(state, player_color):
    score = 0
    legal_moves = getAllLegalMoves(state)
    for move in legal_moves:
        if move_leads_to_capture(state, move, player_color):
            score += 1
    return score

def move_leads_to_capture(state, move, player_color):
    new_state = playMove(state, move)
    if new_state:
        opponent_moves = getAllLegalMoves(new_state)
        for op_move in opponent_moves:
            next_state = playMove(new_state, op_move)
            if next_state and next_state[player_color + 'Capture'] > state[player_color + 'Capture']:
                return True
    return False

# Enhanced game stage determination
def get_game_stage(state):
    thresholds = GAME_STAGE_THRESHOLDS
    total_captured_pieces = state['LightCapture'] + state['DarkCapture']
    total_pieces_on_board = sum(state['Board'])
    total_pieces_initial = 36  # Initial total pieces on the board

    # Mobility
    player_mobility = len(getAllLegalMoves(state))
    opponent_state = copyState(state)
    opponent_state['Turn'] = 'Dark' if state['Turn'] == 'Light' else 'Light'
    opponent_mobility = len(getAllLegalMoves(opponent_state))

    # Calculate average stack size
    num_non_empty_squares = sum(1 for piece in state['Board'] if piece > 0)
    average_stack_size = total_pieces_on_board / num_non_empty_squares if num_non_empty_squares > 0 else 0

    # Determine if large stacks exist
    large_stacks = sum(1 for piece in state['Board'] if piece >= 4)

    # Early game: high mobility, low average stack size, few large stacks
    if (total_captured_pieces < thresholds['early_captured_pieces'] and
        average_stack_size <= thresholds['average_stack_size'] and
        large_stacks < thresholds['large_stacks']):
        return 'early'
    # Mid game: moderate mobility, increasing average stack size
    elif (thresholds['early_captured_pieces'] <= total_captured_pieces < thresholds['mid_captured_pieces'] or
          average_stack_size <= 3):
        return 'mid'
    else:
        # Late game: low mobility, high average stack size, presence of large stacks
        return 'late'

def is_initial_state(state):
    # Check if the board is in its initial configuration
    return sum(state['Board']) == 36 and state['LightCapture'] == 0 and state['DarkCapture'] == 0

def select_opening_move(state):
    # Define a list of strong opening moves
    possible_openings = [
        {'Row': 2, 'Col': 2, 'Direction': 'SE'},
        {'Row': 2, 'Col': 3, 'Direction': 'SW'},
        {'Row': 3, 'Col': 2, 'Direction': 'NE'},
        {'Row': 3, 'Col': 3, 'Direction': 'NW'},
        # Add more opening moves as needed
    ]
    for move in possible_openings:
        if isLegal(state, move):
            return move
    return None

# Minimax function with alpha-beta pruning and dynamic depth in late game
def minimax(state, depth, alpha, beta, maximizingPlayer, player_color, game_stage, start_time, time_limit):
    # Time check to avoid exceeding time limit
    if time.time() - start_time > time_limit:
        return eval(state, player_color, game_stage), None

    if depth == 0 or isGameOver(state):
        return eval(state, player_color, game_stage), None

    legal_moves = getAllLegalMoves(state)
    if not legal_moves:
        # No legal moves, game over
        return eval(state, player_color, game_stage), None

    if maximizingPlayer:
        maxEval = float('-inf')
        best_move = None
        for move in legal_moves:
            new_state = playMove(state, move)
            if new_state is None:
                continue
            eval_value, _ = minimax(new_state, depth - 1, alpha, beta, False, player_color, game_stage, start_time, time_limit)
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
            eval_value, _ = minimax(new_state, depth - 1, alpha, beta, True, player_color, game_stage, start_time, time_limit)
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

    # Determine game stage
    game_stage = get_game_stage(state)

    # Adjust depth and time limit based on game stage
    depth = DEPTHS.get(game_stage, 3)
    time_limit = TIME_LIMITS.get(game_stage, 5)

    start_time = time.time()
    best_move = None

    # Opening move heuristics
    if game_stage == 'early' and is_initial_state(state):
        move = select_opening_move(state)
        if move:
            print(f"STRATEGIC MINIMAX AI SELECTED OPENING MOVE: {move}")
            return move

    # Iterative deepening in late game
    if game_stage == 'late':
        for d in range(1, depth + 1):
            eval_value, move = minimax(state, d, float('-inf'), float('inf'), True, player_color, game_stage, start_time, time_limit)
            if time.time() - start_time > time_limit:
                break
            if move is not None:
                best_move = move
    else:
        # Regular minimax search
        eval_value, best_move = minimax(state, depth, float('-inf'), float('inf'), True, player_color, game_stage, start_time, time_limit)

    if best_move:
        print(f"STRATEGIC MINIMAX AI ({game_stage.upper()} STAGE) SELECTED MOVE: {best_move}")
        return best_move

    # Fallback to random move if no best move found
    legal_moves = getAllLegalMoves(state)
    move = random.choice(legal_moves)
    print(f"STRATEGIC MINIMAX AI SELECTED RANDOM MOVE: {move}")
    return move
