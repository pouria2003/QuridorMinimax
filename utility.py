from Board import Board
from Player import Player
# import numpy as np


def utility(board: Board, player: Player, opponent: Player):
    value = 0
    if player.terminal_test():
        value += 1000000

    # value += board.shortestPath(opponent) - board.shortestPath(player) * 1.1


    if player.name == 'player 1':
        value += board.shortestPath(opponent) - board.shortestPath(player) * 1.1
    else :
        # value += 1./(board.shortestPath(player) * 1.1) - 1./board.shortestPath(opponent)
        value += board.shortestPath(opponent) - board.shortestPath(player) * 2


    return value
