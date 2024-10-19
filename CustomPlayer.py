import random
from GameRules import *
import time

# AI name
def name():
    return 'StrategicMinimaxAI'


# parameter set 10 from first run thru, won %80 of time
EVAL_WEIGHTS = {
    'pieces': 1.0,
    'captured': 2.0,  # Highly prioritize captures
    'middle_pieces': 3.0,
    'largest_stack_penalty': 0.2,
    'potential_captures': 2.0,  # Increase potential captures weight
    'mobility': 2.0,  # Highly prioritize mobility
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

# function to set parameters from outside, helper for testAIplayers (not nessecary for playing regular games)
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

# evaluation function
def eval(state, player_color, game_stage):
    opponent_color = 'Dark' if player_color == 'Light' else 'Light'

    # total number of pieces on the board
    player_pieces = 0
    opponent_pieces = 0

    # number of pieces in the middle of the board
    player_middle_pieces = 0
    opponent_middle_pieces = 0

    # mobility (number of legal moves)
    player_mobility = len(getAllLegalMoves(state)) if state['Turn'] == player_color else 0
    opponent_state = copyState(state)
    opponent_state['Turn'] = opponent_color
    opponent_mobility = len(getAllLegalMoves(opponent_state))

    middle_rows = [2, 3]
    middle_cols = [2, 3]

    # largest stack size
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

    # use weights from EVAL_WEIGHTS
    weights = EVAL_WEIGHTS

    # parameter evaluation based on game stage
    if game_stage == 'early':
        eval_value = (
            weights['pieces'] * (player_pieces + player_captured - opponent_pieces - opponent_captured)
            + weights['middle_pieces'] * (player_middle_pieces - opponent_middle_pieces)
            - weights['largest_stack_penalty'] * max(0, player_largest_stack - 3)
            + weights['potential_captures'] * potential_capture_score(state, player_color)
        )
    elif game_stage == 'mid':
        eval_value = (
            weights['pieces'] * (player_pieces + 2 * player_captured - opponent_pieces - 2 * opponent_captured)
            + weights['mobility'] * (player_mobility - opponent_mobility)
        )
    else:
        eval_value = (
            weights['pieces'] * (player_pieces + 3 * player_captured - opponent_pieces - 3 * opponent_captured)
            + weights['mobility'] * (player_mobility - opponent_mobility) * 2
            + weights['largest_stack_bonus'] * player_largest_stack
        )

    return eval_value

# calculate potential capture score
def potential_capture_score(state, player_color):
    score = 0
    legal_moves = getAllLegalMoves(state)
    for move in legal_moves:
        if move_leads_to_capture(state, move, player_color):
            score += 1
    return score

#moves that lead to capturing
def move_leads_to_capture(state, move, player_color):
    new_state = playMove(state, move)
    if new_state:
        opponent_moves = getAllLegalMoves(new_state)
        for op_move in opponent_moves:
            next_state = playMove(new_state, op_move)
            if next_state and next_state[player_color + 'Capture'] > state[player_color + 'Capture']:
                return True
    return False

# game stage determination
def get_game_stage(state):
    thresholds = GAME_STAGE_THRESHOLDS
    total_captured_pieces = state['LightCapture'] + state['DarkCapture']
    total_pieces_on_board = sum(state['Board'])
    total_pieces_initial = 36  # initial total pieces on the board

    # mobility
    player_mobility = len(getAllLegalMoves(state))
    opponent_state = copyState(state)
    opponent_state['Turn'] = 'Dark' if state['Turn'] == 'Light' else 'Light'
    opponent_mobility = len(getAllLegalMoves(opponent_state))

    # calculate average stack size
    num_non_empty_squares = sum(1 for piece in state['Board'] if piece > 0)
    average_stack_size = total_pieces_on_board / num_non_empty_squares if num_non_empty_squares > 0 else 0

    # determine if large stacks exist
    large_stacks = sum(1 for piece in state['Board'] if piece >= 4)

    if (total_captured_pieces < thresholds['early_captured_pieces'] and
        average_stack_size <= thresholds['average_stack_size'] and
        large_stacks < thresholds['large_stacks']):
        return 'early'
    elif (thresholds['early_captured_pieces'] <= total_captured_pieces < thresholds['mid_captured_pieces'] or
          average_stack_size <= 3):
        return 'mid'
    else:
        return 'late'

def is_initial_state(state):
    # check if the board is in its initial configuration
    return sum(state['Board']) == 36 and state['LightCapture'] == 0 and state['DarkCapture'] == 0

def select_opening_move(state):
    # list of strong opening moves
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

# minimax function with alpha-beta pruning and dynamic depth in late game
def minimax(state, depth, alpha, beta, maximizingPlayer, player_color, game_stage, start_time, time_limit):
    # time check to avoid exceeding time limit
    if time.time() - start_time > time_limit:
        return eval(state, player_color, game_stage), None

    if depth == 0 or isGameOver(state):
        return eval(state, player_color, game_stage), None

    legal_moves = getAllLegalMoves(state)
    if not legal_moves:
        # no legal moves, game over
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

    # determine game stage
    game_stage = get_game_stage(state)

    # adjust depth and time limit based on game stage
    depth = DEPTHS.get(game_stage, 3)
    time_limit = TIME_LIMITS.get(game_stage, 5)

    start_time = time.time()
    best_move = None

    # opening move heuristics
    if game_stage == 'early' and is_initial_state(state):
        move = select_opening_move(state)
        if move:
            print(f"STRATEGIC MINIMAX AI SELECTED OPENING MOVE: {move}")
            return move

    # iterative deepening in late game
    if game_stage == 'late':
        for d in range(1, depth + 1):
            eval_value, move = minimax(state, d, float('-inf'), float('inf'), True, player_color, game_stage, start_time, time_limit)
            if time.time() - start_time > time_limit:
                break
            if move is not None:
                best_move = move
    else:
        # regular minimax search
        eval_value, best_move = minimax(state, depth, float('-inf'), float('inf'), True, player_color, game_stage, start_time, time_limit)

    if best_move:
        print(f"STRATEGIC MINIMAX AI ({game_stage.upper()} STAGE) SELECTED MOVE: {best_move}")
        return best_move

    # fallback to random move if no best move found
    legal_moves = getAllLegalMoves(state)
    move = random.choice(legal_moves)
    print(f"STRATEGIC MINIMAX AI SELECTED RANDOM MOVE: {move}")
    return move
