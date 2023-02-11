#   Two players throw small sharp-pointed missiles known as darts at a round target known as a dartboard.
#   Who is going to win this game?
#   You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:

#                       1	2	3	4	5	6	7
#                       24	D	D	D	D	D	8
#                       23	D	T	T	T	D	9
#                       22	D	T	B	T	D	10
#                       21	D	T	T	T	D	11
#                       20	D	D	D	D	D	12
#                       19	18	17	16	15	14	13
#
#   Each of the two players starts with a score of 501, and they take turns to throw a dart – one throw for each player.
#   The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero
#   or less wins the game.
#   You are going to receive the information for every throw on a separate line. The coordinate information of a hit
#   will be in the format: "({row}, {column})".
#   •	If a player hits outside the dartboard, he does not score any points.
#   •	If a player hits a number, it is deducted from his total.
#   •	If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted
#       from his total.
#   •	If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted
#       from his total.
#   •	"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
#   For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are
#   deducted from his total.
#   Your job is to find who won the game and with how many turns.
#   Input
#   •	The name of the first player and the name of the second player, separated by ", "
#   •	7 lines – the dartboard (separated by single space)
#   •	On the next lines - the coordinates in the format: "({row}, {column})"
#   Output
#   •	You should print only one line containing the winner and his count of throws:
#       "{name} won the game with {count_turns} throws!"
#   Constrains
#   •	There will always be exactly 7 lines
#   •	There will always be a winner
#   •	The points will be in range [1, 24]
#   •	The coordinates will be in range [0, 100]

from collections import deque


def get_coordinates():
    position = input()
    position = position.replace("(", "")
    position = position.replace(")", "")
    position = [int(x) for x in position.split(", ")]
    return position


def throw_a_dart(row, col):
    current_player = player_names.popleft()
    player_names.append(current_player)
    player_throws[current_player] += 1

    if 0 <= row < size and 0 <= col < size:

        if darts_board[row][col] == "B":
            print(f"{current_player} won the game with {player_throws[current_player]} throws!")
            return True
        elif darts_board[row][col] == "T":
            player_points[current_player] -= 3 * (
                    darts_board[row][0] + darts_board[row][size - 1] +
                    darts_board[0][col] + darts_board[size - 1][col]
            )
        elif darts_board[row][col] == "D":
            player_points[current_player] -= 2 * (
                    darts_board[row][0] + darts_board[row][size - 1] +
                    darts_board[0][col] + darts_board[size - 1][col]
            )
        else:
            player_points[current_player] -= darts_board[row][col]

        if player_points[current_player] <= 0:
            print(f"{current_player} won the game with {player_throws[current_player]} throws!")
            return True


player_names = deque(input().split(", "))
size = 7
darts_board = [[int(x) if x.isdigit() else str(x) for x in input().split()] for row in range(size)]

player_points = {
    player_names[0]: 501,
    player_names[1]: 501,
}

player_throws = {
    player_names[0]: 0,
    player_names[1]: 0,
}

player_won = False

while not player_won:
    r, c = get_coordinates()
    player_won = throw_a_dart(r, c)



