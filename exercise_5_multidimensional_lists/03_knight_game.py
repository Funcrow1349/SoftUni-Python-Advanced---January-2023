#   Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task -
#   the Knight.
#   A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the
#   same row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can
#   move one square horizontally then two squares vertically - i.e., in an "L" pattern.)
#   The knight game is played on a board with dimensions N x N.
#   You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no
#   knights that can attack one another with one move are left.
#   Always remove the knight who can attack the greatest number of knights. If there are two or more knights with the
#   same number of attacks, remove the top-left one.
#   Input
#   •	On the first line, you will receive integer N - the size of the board
#   •	On the following N lines, you will receive strings with "K" and "0"
#   Output
#   •	Print a single integer with the number of knights that need to be removed.
#   Constraints
#   •	The size of the board will be 0 < N < 30
#   •	Time limit: 0.3 sec. Memory limit: 16 MB

def knights_func(dimensions):
    positions = []
    for row in range(dimensions):
        for col in range(dimensions):
            if chess_board[row][col] == "K":
                positions.append((row, col))
    return positions


board_dimensions = int(input())
chess_board = [list(input()) for row in range(board_dimensions)]
knights_positions = knights_func(board_dimensions)

directions = (
    (-2, -1),        # top-left
    (-2, 1),         # top-right
    (-1, -2),        # top-mid-left
    (-1, 2),         # top-mid-right
    (1, -2),         # low-mid-left
    (1, 2),          # low-mid-right
    (2, -1),         # low-left
    (2, 1),          # low-right
)

removed_knights = 0

while knights_positions:
    possible_attacks_dict = {}
    for knight in knights_positions:
        possible_attacks = 0
        for direction in directions:
            x, y = knight[0] + direction[0], knight[1] + direction[1]
            if 0 <= x < board_dimensions and 0 <= y < board_dimensions:
                if chess_board[x][y] == "K":
                    possible_attacks += 1
        if possible_attacks not in possible_attacks_dict and possible_attacks > 0:
            possible_attacks_dict[possible_attacks] = knight

    if not possible_attacks_dict:
        break

    knight_to_remove = max(possible_attacks_dict)
    knights_positions.remove(possible_attacks_dict[knight_to_remove])
    chess_board[possible_attacks_dict[knight_to_remove][0]][possible_attacks_dict[knight_to_remove][1]] = 0
    possible_attacks_dict = {}
    removed_knights += 1

print(removed_knights)












