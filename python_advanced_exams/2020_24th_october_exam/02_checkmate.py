#   You will be given a chess board (8x8). On the board there will be 3 types of symbols:
#   •	"." – empty square
#   •	"Q" – a queen
#   •	"K" – the king
#   Your job is to find which queens can capture the king and print them. The moves that the queen can do is to move
#   diagonally, horizontally and vertically (basically all the moves that all the other figures can do except from the
#   knight). Beware that there might be queens that stand in the way of other queens and can stop them from capturing
#   the king. For more clarification see the examples.
#   Input
#   •	8 lines – the state of the board (each square separated by single space)
#   Output
#   •	The positions of the queens that can capture the king as lists
#   •	If the king cannot be captured, print: "The king is safe!"
#   •	The order of output does not matter
#   Constrains
#   •	There will always be exactly 8 lines
#   •	There will always be exactly one King
#   •	Only the 3 symbols described above will be present in the input

chess_board = [[x for x in input().split()]for i in range(8)]
queens_positions = []
kings_position = []

for row in range(len(chess_board)):
    for col in range(len(chess_board)):
        if chess_board[row][col] == "Q":
            queens_positions.append([row, col])

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "top_left": (-1, -1),
    "top_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1),
}
check_mate = False

for pos in queens_positions:

    for direction in directions.keys():
        row, col = pos[0] + directions[direction][0], pos[1] + directions[direction][1]

        while 0 <= row < len(chess_board) and 0 <= col < len(chess_board):
            if chess_board[row][col] == "Q":
                break
            if chess_board[row][col] == "K":
                check_mate = True
                print(pos)
                break

            row += directions[direction][0]
            col += directions[direction][1]


if not check_mate:
    print("The king is safe!")