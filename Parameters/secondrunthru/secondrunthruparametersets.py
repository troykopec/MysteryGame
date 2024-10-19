# List of new parameter sets to test
new_parameter_sets = [
    # Parameter Set A: Increase Aggression
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.5,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.5,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set B: Enhance Mobility
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 2.5,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set C: Balance Aggression and Defense
    {
        'eval_weights': {
            'pieces': 1.2,
            'captured': 1.8,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 1.8,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set D: Focus on Middle Control
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 4.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set E: Reduce Largest Stack Penalty
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.1,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set F: Increase Largest Stack Bonus
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 2.0,
        }
    },
    # Parameter Set G: Adjust Game Stage Depths
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        },
        'depths': {
            'early': 4,
            'mid': 4,
            'late': 7,
        }
    },
    # Parameter Set H: Decrease Time Limits
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        },
        'time_limits': {
            'early': 3,
            'mid': 5,
            'late': 10,
        }
    },
    # Parameter Set I: Adjust Game Stage Thresholds
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        },
        'thresholds': {
            'early_captured_pieces': 5,
            'mid_captured_pieces': 20,
            'average_stack_size': 1.5,
            'large_stacks': 2,
        }
    },
    # Parameter Set J: Emphasize Own Pieces
    {
        'eval_weights': {
            'pieces': 1.5,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set K: Decrease Middle Control Emphasis
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 2.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set L: Increase Penalty for Large Stacks
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.5,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set M: Emphasize Potential Captures Even More
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 3.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set N: Reduce Importance of Own Pieces
    {
        'eval_weights': {
            'pieces': 0.8,
            'captured': 2.0,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 2.0,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set O: Adjust Mobility and Captured Balance
    {
        'eval_weights': {
            'pieces': 1.0,
            'captured': 2.5,
            'middle_pieces': 3.0,
            'largest_stack_penalty': 0.2,
            'potential_captures': 2.0,
            'mobility': 1.5,
            'largest_stack_bonus': 1.0,
        }
    },
    # Parameter Set P: Combine Multiple Adjustments
    {
        'eval_weights': {
            'pieces': 1.2,
            'captured': 2.2,
            'middle_pieces': 3.5,
            'largest_stack_penalty': 0.1,
            'potential_captures': 2.2,
            'mobility': 2.2,
            'largest_stack_bonus': 1.5,
        },
        'depths': {
            'early': 4,
            'mid': 4,
            'late': 7,
        },
        'time_limits': {
            'early': 4,
            'mid': 8,
            'late': 12,
        }
    },
]
