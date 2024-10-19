# TestAIPlayers.py

import subprocess
import re
import multiprocessing
import itertools
import os
import sys

# Import your custom player module
# Note: We will import CustomPlayer within each process
# to ensure that each process has its own copy
# This avoids issues with shared state across processes

from parametersets import new_parameter_sets as parameter_sets  # Import parameter sets

# List of AI player modules
ai_players = [
    'MiniMax',
    'AggressiveCaptureAI',
    'DefensiveMobilityAI',
    'StackBuilderAI'
]

# Custom player module name
custom_player = 'CustomPlayer'

# Function to parse the game output and extract the outcome
def parse_game_output(game_output, light_player_name, dark_player_name):
    # Split the output into lines
    lines = game_output.strip().split('\n')

    light_captures = None
    dark_captures = None
    game_over = False

    for i, line in enumerate(lines):
        line = line.strip()

        if 'GAME OVER' in line:
            game_over = True
            # Look for the final 'Captures: X Light and Y Dark'
            for j in range(i, -1, -1):  # Loop backwards to find the captures line before GAME OVER
                previous_line = lines[j].strip()
                if previous_line.startswith('Captures:'):
                    match = re.match(r'Captures:\s+(\d+)\s+Light\s+and\s+(\d+)\s+Dark', previous_line)
                    if match:
                        light_captures = int(match.group(1))
                        dark_captures = int(match.group(2))
                    break
            break

    if game_over and light_captures is not None and dark_captures is not None:
        if light_captures > dark_captures:
            winner_name = light_player_name
        elif dark_captures > light_captures:
            winner_name = dark_player_name
        else:
            winner_name = 'Draw'
    else:
        winner_name = 'Unknown'

    return winner_name, light_captures, dark_captures

# Function to play a game and return the outcome
def play_game(args):
    # Unpack arguments
    params, ai_player, game_role, game_number, total_games = args

    # Set parameters in CustomPlayer within this process
    # We need to import CustomPlayer here to ensure it's in the current process
    import CustomPlayer
    CustomPlayer.set_parameters(
        eval_weights=params.get('eval_weights'),
        depths=params.get('depths'),
        time_limits=params.get('time_limits'),
        thresholds=params.get('thresholds')
    )

    # Determine players based on game_role
    if game_role == 'CustomLight':
        light_player = custom_player
        dark_player = ai_player
        light_player_name = custom_player
        dark_player_name = ai_player
    else:
        light_player = ai_player
        dark_player = custom_player
        light_player_name = ai_player
        dark_player_name = custom_player

    command = ['python3', 'GameEngine.py', light_player, dark_player, str(game_number)]
    try:
        # Run the game and capture the output
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        game_output = result.stdout
        winner_name, light_captures, dark_captures = parse_game_output(game_output, light_player_name, dark_player_name)
        outcome = {
            'Winner': winner_name,
            'LightCaptures': light_captures,
            'DarkCaptures': dark_captures,
            'Parameters': params,
            'GameRole': game_role,
            'AIPlayer': ai_player,
            'GameNumber': game_number
        }
    except subprocess.CalledProcessError as e:
        outcome = {
            'Winner': 'Error',
            'ErrorMessage': f"An error occurred while running the game: {e}\nOutput:\n{e.output}",
            'Parameters': params,
            'GameRole': game_role,
            'AIPlayer': ai_player,
            'GameNumber': game_number
        }
    # Print progress update
    print(f"({game_number + 1}/{total_games}) games completed")
    return outcome

def main():
    manager = multiprocessing.Manager()
    game_number = 0
    results = []

    # Number of games per parameter set
    num_repeats = 5  # Adjust as needed

    total_games = len(parameter_sets) * len(ai_players) * 2 * num_repeats

    # Create a list of all games to be played
    games_to_play = []

    for params in parameter_sets:
        for _ in range(num_repeats):
            for ai_player in ai_players:
                # CustomPlayer is Light, AI Player is Dark
                game_role = 'CustomLight'
                games_to_play.append((params, ai_player, game_role, game_number, total_games))
                game_number += 1

                # AI Player is Light, CustomPlayer is Dark
                game_role = 'CustomDark'
                games_to_play.append((params, ai_player, game_role, game_number, total_games))
                game_number += 1

    # Reset game_number for progress tracking
    game_number = 0

    # Use multiprocessing Pool to run games in parallel
    num_workers = multiprocessing.cpu_count()  # Use the number of available CPU cores
    with multiprocessing.Pool(processes=num_workers) as pool:
        for outcome in pool.imap_unordered(play_game, games_to_play):
            results.append(outcome)
            game_number += 1

    # Aggregate results
    aggregated_results = {}

    for outcome in results:
        params = outcome['Parameters']
        params_key = str(params)  # Convert params to a string to use as a key
        if params_key not in aggregated_results:
            aggregated_results[params_key] = {
                'Parameters': params,
                'Wins': 0,
                'Losses': 0,
                'Draws': 0,
                'Total Games': 0
            }
        aggregated_results[params_key]['Total Games'] += 1

        if custom_player in outcome['Winner']:
            aggregated_results[params_key]['Wins'] += 1
        elif 'Draw' in outcome['Winner']:
            aggregated_results[params_key]['Draws'] += 1
        else:
            aggregated_results[params_key]['Losses'] += 1

    # After testing all parameter sets, display the results
    for result in aggregated_results.values():
        print()
        print(f"Parameters: {result['Parameters']}")
        print(f"Wins: {result['Wins']}, Losses: {result['Losses']}, Draws: {result['Draws']}")
        win_rate = result['Wins'] / result['Total Games'] * 100
        print(f"Win Rate: {win_rate:.2f}%")
        print("-" * 50)

if __name__ == '__main__':
    main()
