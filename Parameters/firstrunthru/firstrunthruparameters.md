# AI Parameter Sets

## Parameter Set 1: Base Parameters
- **Description**: The base parameter set used as a default configuration.

## Parameter Set 2: Aggressive Capture Focus
- **Changes**: Increased weight on `captured` and `potential_captures`.
- **Effect**: AI prioritizes capturing opponent pieces and setting up potential captures, potentially leading to a more aggressive play style.

## Parameter Set 3: Mobility Focus
- **Changes**: Increased weight on `mobility`.
- **Effect**: AI favors positions with more legal moves, leading to better flexibility and avoidance of traps.

## Parameter Set 4: Deemphasized Center Control
- **Changes**: Reduced emphasis on `middle_pieces`.
- **Effect**: AI focuses less on controlling the center and more on other strategies, such as capturing or defending.

## Parameter Set 5: Cautious Stack Management
- **Changes**: Increased penalty for large stacks.
- **Effect**: AI avoids creating vulnerable stacks that can be captured by the opponent, leading to a more cautious approach.

## Parameter Set 6: Largest Stack Bonus
- **Changes**: Increased `largest_stack_bonus`.
- **Effect**: AI is rewarded for having large stacks, which can be advantageous in the late game when controlling key positions is crucial.

## Parameter Set 7: Improved Early Game
- **Changes**: Increased early game search depth.
- **Effect**: AI makes better opening moves, leading to improved positioning from the start.

## Parameter Set 8: Time Pressure
- **Changes**: Reduced time limits.
- **Effect**: AI is forced to make quicker decisions, simulating time pressure or time-sensitive scenarios.

## Parameter Set 9: Early Game Stage Transition
- **Changes**: Adjusted game stage thresholds for earlier mid and late game.
- **Effect**: AI enters the mid and late game stages earlier, potentially catching opponents off guard with strategic shifts.

## Parameter Set 10: Aggressive and Dynamic Play
- **Changes**: Increased weights on `captured`, `potential_captures`, and `mobility`.
- **Effect**: AI adopts a highly aggressive and dynamic play style.

## Parameter Set 11: Defensive Play Focus
- **Changes**: Emphasized `pieces`.
- **Effect**: AI focuses on preserving its own pieces, leading to a more defensive strategy.

## Parameter Set 12: Sacrificial Strategy
- **Changes**: Deemphasized `pieces`.
- **Effect**: AI is more willing to sacrifice pieces for strategic advantages elsewhere.

## Parameter Set 13: Unconventional Strategy
- **Changes**: Significantly reduced weight on `middle_pieces`.
- **Effect**: AI focuses less on controlling the center, potentially leading to unconventional strategies.

## Parameter Set 14: Deeper Search Depths
- **Changes**: Increased search depths across all game stages.
- **Effect**: AI can look further ahead, improving decision-making at the cost of longer computation times.

## Parameter Set 15: Anticipation of Capture Opportunities
- **Changes**: Emphasized `potential_captures`.
- **Effect**: AI is better at anticipating future capture opportunities and setting up advantageous positions.
