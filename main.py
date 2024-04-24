from Player import Player
from Board import Board
from Action import Action, doAction
from AI import AI

size = 7
depth = 6
player2 = Player(8, 'player 2', 0, size - 1)
player1 = Player(8, 'player 1', size * 2 - 2, size - 1)

board = Board(size, player1, player2)

board.displayboard()

Round=0

print()
print()
print()

player1_ai = AI()
player2_ai = AI()

isPalyer2 = False

while True:
    if isPalyer2:
        ai_action = player2_ai.choose_action(board, player2, player1, depth)

        doAction(ai_action, player2, board)

        if ai_action.direction == "vertical":
            print(f"AI {player2.name} chose to place a vertical wall at [{ai_action.row}][{ai_action.column}]:")
            print()
        elif ai_action.direction == "horizontal":
            print(f"AI {player2.name} chose to place a horizontal wall at [{ai_action.row}][{ai_action.column}]:")
            print()
        else:
            print(
                f"AI {player2.name} chose to go {ai_action.direction}:"
            )
            print()

    else:
            ai_action = player1_ai.choose_action(board, player1, player2, depth)

            doAction(ai_action, player1, board)

            if ai_action.direction == "vertical":
                print(f"AI {player1.name} chose to place a vertical wall at [{ai_action.row}][{ai_action.column}]:")
                print()
            elif ai_action.direction == "horizontal":
                print(f"AI {player1.name} chose to place a horizontal wall at [{ai_action.row}][{ai_action.column}]:")
                print()
            else:
                print(
                    f"AI {player1.name} chose to go {ai_action.direction}:"
                )
                print()

    board.displayboard()

    if player1.terminal_test():
        print(f"{player1.name} wins!")
        exit()
    if player2.terminal_test():
        print(f"{player2.name} wins!")
        exit()

    isPalyer2 = not isPalyer2
    Round+=1
    print("Round: " + str(Round))
