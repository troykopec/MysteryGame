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





# Parameter sets to test
winner = [
    # Parameter Set 1 (Base)
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
    }
]


# Parameter sets to test
threshold_test = [
    # Parameter Set 1 (Base)
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
    # Parameter Set 2: Enter Mid Game Earlier
    {
        'thresholds': {
            'early_captured_pieces': 5,   # Decrease to enter mid game earlier
            'mid_captured_pieces': 20,    # Decrease to enter late game earlier
            'average_stack_size': 1.5,
            'large_stacks': 3,
        }
    },
    # Parameter Set 3: Delayed Game Stage Transitions
    {
        'thresholds': {
            'early_captured_pieces': 15,  # Increase to stay in early game longer
            'mid_captured_pieces': 35,    # Increase to stay in mid game longer
            'average_stack_size': 1.5,
            'large_stacks': 3,
        }
    },
    # Parameter Set 4: Focus on Stack Size for Game Stages
    {
        'thresholds': {
            'early_captured_pieces': 10,
            'mid_captured_pieces': 30,
            'average_stack_size': 2.0,    # Increase to shift stages based on larger stacks
            'large_stacks': 4,            # Increase to consider more large stacks
        }
    },
    # Parameter Set 5: Emphasize Large Stack Count
    {
        'thresholds': {
            'early_captured_pieces': 10,
            'mid_captured_pieces': 30,
            'average_stack_size': 1.5,
            'large_stacks': 2,            # Decrease to transition stages when fewer large stacks are present
        }
    },
    # Parameter Set 6: Aggressive Early Game Transition
    {
        'thresholds': {
            'early_captured_pieces': 3,   # Very early transition to mid game
            'mid_captured_pieces': 15,    # Early transition to late game
            'average_stack_size': 1.5,
            'large_stacks': 2,
        }
    },
    # Parameter Set 7: Balanced Game Stage Thresholds
    {
        'thresholds': {
            'early_captured_pieces': 8,
            'mid_captured_pieces': 25,
            'average_stack_size': 1.7,
            'large_stacks': 3,
        }
    },
    # Parameter Set 8: Late Transition to Late Game
    {
        'thresholds': {
            'early_captured_pieces': 10,
            'mid_captured_pieces': 40,    # Delay transition to late game
            'average_stack_size': 1.5,
            'large_stacks': 3,
        }
    },
    # Parameter Set 9: Emphasize Average Stack Size
    {
        'thresholds': {
            'early_captured_pieces': 10,
            'mid_captured_pieces': 30,
            'average_stack_size': 2.0,    # Transition stages when average stack size increases
            'large_stacks': 3,
        }
    },
    # Parameter Set 10: Early Game Focus on Large Stacks
    {
        'thresholds': {
            'early_captured_pieces': 10,
            'mid_captured_pieces': 30,
            'average_stack_size': 1.5,
            'large_stacks': 1,            # Transition stages when any large stacks appear
        }
    },
    # Parameter Set 11: Combine Early Mid Game Transition and Stack Size Emphasis
    {
        'thresholds': {
            'early_captured_pieces': 5,    # Early transition to mid game
            'mid_captured_pieces': 25,
            'average_stack_size': 1.8,     # Transition based on slightly larger average stack size
            'large_stacks': 2,
        }
    },
    # Parameter Set 12: Strict Transition Conditions
    {
        'thresholds': {
            'early_captured_pieces': 12,   # Later transition to mid game
            'mid_captured_pieces': 35,     # Later transition to late game
            'average_stack_size': 2.5,     # Only transition if average stack size is significantly larger
            'large_stacks': 5,             # Require more large stacks for transition
        }
    },
]