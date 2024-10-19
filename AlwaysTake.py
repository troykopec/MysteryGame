## This is an example player who makes moves randomly

import GameRules
import random

def name():
    return 'Always Take'

# Returns a random legal move 
def getMove(state):
    legal_moves = GameRules.getAllLegalMoves(state)
    for move in legal_moves:
        direction = move['Direction'] 
        if len(direction) < 2:
            print("ALWAYS TAKE TAKING : " + direction)
            return move
 
    move = random.choice(legal_moves)
    print("ALWAYS TAKE TAKING : " + move['Direction'] )   
    return move
