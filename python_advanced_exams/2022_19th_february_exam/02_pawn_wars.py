#   A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are
#   marked from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a
#   number (a1, b1, c1, etc.). In this problem colors of the board will be ignored.
#   We will play the game with two pawns, white (w) and black (b), where they can:
#   •	Only move forward in a straight line:
#       	White (w) moves from the 1st rank to the 8th rank direction.
#       	Black (b) moves from 8th rank to the 1st rank direction.
#   •	Can move only 1 square at a time.
#   •	Can capture another pawn in from of them only diagonally:
#   When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the
#   1st rank), can be promoted to a queen.
#   Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white
#   pawn (w), then black moves (b), then white (w) again, and so on.
#   Some rules apply when moving paws:
#   •	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn
#       captures another pawn, the game is over.
#   •	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
#   Input
#   •	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
#       o	Empty positions are marked with "-".
#       o	White pawn is marked with "w"
#       o	Black pawn is marked with "b"
#   Output
#   Print either one of the following:
#   •	If a pawn captures the other, print:
#       o	"Game over! {White/Black} win, capture on {square}."
#   •	If a pawn reaches the last rank, print:
#   o	"Game over! {White/Black} pawn is promoted to a queen at {square}."
#   Constraints
#   •	The input will always be valid.
#   •	The matrix will always be 8x8.
#   •	There will be no case where two pawns are placed on the same square.
#   •	There will be no case where two pawns are placed on the same column.
#   •	There will be no case where black/white will be placed on the last rank.

def find_chessboard_pos(pawn):
    horizontal = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
    vertical = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
    return f"{horizontal[pawn[1]]}{vertical[pawn[0]]}"


chessboard = []
white_pawn = []
black_pawn = []

for i in range(8):
    row = input().split()
    chessboard.append(row)
    if "w" in row:
        white_pawn = [i, row.index("w")]
    if "b" in row:
        black_pawn = [i, row.index("b")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1),
}

while white_pawn[0] > 0 and black_pawn[0] < 7:
    up_left_row, up_left_col = white_pawn[0] + directions["up_left"][0], white_pawn[1] + directions["up_left"][1]
    up_right_row, up_right_col = white_pawn[0] + directions["up_right"][0], white_pawn[1] + directions["up_right"][1]
    up_row, up_col = white_pawn[0] + directions["up"][0], white_pawn[1] + directions["up"][1]

    down_left_row, down_left_col = black_pawn[0] + directions["down_left"][0], black_pawn[1] + directions["down_left"][1]
    down_right_row, down_right_col = black_pawn[0] + directions["down_right"][0], black_pawn[1] + directions["down_right"][1]
    down_row, down_col = black_pawn[0] + directions["down"][0], black_pawn[1] + directions["down"][1]

    if 0 <= up_left_row < len(chessboard) and 0 <= up_left_col < len(chessboard):
        if chessboard[up_left_row][up_left_col] == "b":
            white_pawn = [up_left_row, up_left_col]
            print(f"Game over! White win, capture on {find_chessboard_pos(white_pawn)}.")
            break

    if 0 <= up_right_row < len(chessboard) and 0 <= up_right_col < len(chessboard):
        if chessboard[up_right_row][up_right_col] == "b":
            white_pawn = [up_right_row, up_right_col]
            print(f"Game over! White win, capture on {find_chessboard_pos(white_pawn)}.")
            break

    chessboard[white_pawn[0]][white_pawn[1]] = "-"
    white_pawn = [up_row, up_col]
    chessboard[up_row][up_col] = "w"

    if up_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {find_chessboard_pos(white_pawn)}.")
        break

    if 0 <= down_left_row < len(chessboard) and 0 <= down_left_col < len(chessboard):
        if chessboard[down_left_row][down_left_col] == "w":
            black_pawn = [down_left_row, down_left_col]
            print(f"Game over! Black win, capture on {find_chessboard_pos(black_pawn)}.")
            break

    if 0 <= down_right_row < len(chessboard) and 0 <= down_right_col < len(chessboard):
        if chessboard[down_right_row][down_right_col] == "w":
            black_pawn = [down_right_row, down_right_col]
            print(f"Game over! Black win, capture on {find_chessboard_pos(black_pawn)}.")
            break

    chessboard[black_pawn[0]][black_pawn[1]] = "-"
    black_pawn = [down_row, down_col]
    chessboard[down_row][down_col] = "b"

    if down_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {find_chessboard_pos(black_pawn)}.")
        break