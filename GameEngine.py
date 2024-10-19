###############
## Matt Lepinski
## Version 1
## Code to support Project 1 for CSC 410 - Fall 2024
###############

## To run a game
##    between the players in Alice.py and Bob.py
##
## python GameEngine.py Alice Bob
##
## By default the output will go into file game0.log
## You can choose a different file as follows
##
## python GameEngine.py Alice Bob X
##
## ... will save the output in gameX.log

import importlib
import sys
import GameRules

# Load the code for the AI players
# Use command line arguments
# If a player isn't provided use 'DefaultPlayer.py'
players = {}
if ( len(sys.argv) > 1):
    players['Light'] = importlib.import_module(sys.argv[1])
else:
    players['Light'] = importlib.import_module('DefaultPlayer')

if ( len(sys.argv) > 2):
    players['Dark'] = importlib.import_module(sys.argv[2])
else:
    players['Dark'] = importlib.import_module('DefaultPlayer')

    
if ( len(sys.argv) > 3):
    log_name = 'game' + sys.argv[3] + '.py'
else:
    log_name = 'game0.log'

# Create a gameID for use in the log file
# Use the 3rd command line argument
# If there are fewer
    
################################

def play_game():
    global players
    global log_name
    
    # open logfile for writing
    logfile = open(log_name, 'w')

    nameLight = players['Light'].name()
    nameDark = players['Dark'].name()
    
    logfile.write(f'Light Player is {nameLight} \n Dark Player is {nameDark} \n')

    state = GameRules.getInitialState()
    startPlayer = state['Turn']
    gameOver = False

    logfile.write(f"{startPlayer} plays first \n")

    while (not gameOver):
        activePlayer = players[ state['Turn'] ]
        move = activePlayer.getMove(state)

        logfile.write(f"Move for {state['Turn']} Player \n")
        logfile.write(str(move))
        print(f"... {move}")
        new_state = GameRules.playMove(state, move)

        if new_state != None:
            state = new_state
            GameRules.printState(state)
            gameOver=GameRules.isGameOver(state)
            if gameOver:
                state = GameRules.endGame(state)
                logfile.write(f"Game Ends. Player {state['Turn']} has no legal moves.\n")
                logfile.write(str(state))
                print(f"\n   GAME OVER. Player {state['Turn']} has no legal moves.")
                GameRules.printState(state)
                
        else:
            gameOver = True
            logfile.write(f"Illegal Move. End of Game \n")
            print(f"Illegal Move {move}. Player {state['Turn']} Forfeits.")

    

        
        
        


# Play a Game Between Two AI Players
play_game()

