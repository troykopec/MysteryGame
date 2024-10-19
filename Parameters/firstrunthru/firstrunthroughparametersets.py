# Parameter sets to test
parameter_sets = [
    # Parameter Set 1 (Base)
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 1.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 1.0,
            'mobility': 1.0,
            'largest_stack_bonus': 1.0,
        },
        'depths': {
            'early': 3,
            'mid': 3,
            'late': 6,
        },
        'time_limits': {
            'early': 5,
            'mid': 10,
            'late': 15,
        },
        'thresholds': {
            'early_captured_pieces': 10,
            'mid_captured_pieces': 30,
            'average_stack_size': 1.5,
            'large_stacks': 3,
        },
    },
    # Parameter Set 2: Emphasize Capturing
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 1.5,  # Increase emphasis on capturing opponent pieces
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 1.5,  # Increase potential captures weight
            'mobility': 1.0,
            'largest_stack_bonus': 1.0,
        },
    },
    # Parameter Set 3: Prioritize Mobility
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 1.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 1.0,
            'mobility': 1.5,  # Increase emphasis on mobility
            'largest_stack_bonus': 1.0,
        },
    },
    # Parameter Set 4: Reduce Middle Control Emphasis
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 1.0,
            'middle_pieces': 2.0,  # Decrease weight on middle control
            'largest_stack_penalty': 0.2,
            'potential_captures': 1.0,
            'mobility': 1.0,
            'largest_stack_bonus': 1.0,
        },
    },
    # Parameter Set 5: Penalize Large Stacks More
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 1.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.5,  # Increase penalty for large stacks
            'potential_captures': 1.0,
            'mobility': 1.0,
            'largest_stack_bonus': 1.0,
        },
    },
    # Parameter Set 6: Reward Large Stacks
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 1.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 1.0,
            'mobility': 1.0,
            'largest_stack_bonus': 2.0,  # Increase bonus for large stacks
        },
    },
    # Parameter Set 7: Increase Search Depth Early Game
    {
        'depths': {
            'early': 4,  # Increase early game search depth
            'mid': 3,
            'late': 6,
        },
    },
    # Parameter Set 8: Faster Decision Making
    {
        'time_limits': {
            'early': 3,  # Reduce time limits
            'mid': 5,
            'late': 10,
        },
    },
    # Parameter Set 9: Enter Mid Game Earlier
    {
        'thresholds': {
            'early_captured_pieces': 5,   # Adjust thresholds to enter mid game earlier
            'mid_captured_pieces': 20,
            'average_stack_size': 1.5,
            'large_stacks': 2,
        },
    },
    # Parameter Set 10: Aggressive Capturing and Mobility
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,  # Highly prioritize captures
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,  # Increase potential captures weight
            'mobility': 2.0,  # Highly prioritize mobility
            'largest_stack_bonus': 1.0,
        },
    },
    # Parameter Set 11: Emphasize Keeping Own Pieces
    {
        'eval_weights': {
            'pieces': 1.5,  # Increase weight on own pieces
            'captured': 1.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 1.0,
            'mobility': 1.0,
            'largest_stack_bonus': 1.0,
        },
    },
    # Parameter Set 12: Deemphasize Own Pieces
    {
        'eval_weights': {
            'pieces': 0.5,  # Decrease weight on own pieces
            'captured': 1.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 1.0,
            'mobility': 1.0,
            'largest_stack_bonus': 1.0,
        },
    },
    # Parameter Set 13: Decrease Middle Control Significantly
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 1.0,
            'middle_pieces': 1.0,  # Significantly reduce middle control emphasis
            'largest_stack_penalty': 0.2,
            'potential_captures': 1.0,
            'mobility': 1.0,
            'largest_stack_bonus': 1.0,
        },
    },
    # Parameter Set 14: Balanced Increased Depth
    {
        'depths': {
            'early': 4,
            'mid': 4,
            'late': 7,
        },
    },
    # Parameter Set 15: Emphasize Potential Captures
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 1.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,  # Increase weight on potential captures
            'mobility': 1.0,
            'largest_stack_bonus': 1.0,
        },
    },
]
