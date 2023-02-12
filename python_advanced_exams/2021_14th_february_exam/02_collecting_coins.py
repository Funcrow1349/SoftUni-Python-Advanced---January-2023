#   You are playing a game, and your goal is to collect 100 coins.
#   On the first line, you will be given a number representing the size of the field with a square shape. On the
#   following few lines, you will be given the field with:
#   •	One player - randomly placed in it and marked with the symbol "P"
#   •	Numbers for coins placed at different positions of the field
#   •	Walls marked with "X"
#   After the field state, you will be given commands for the player's movement. Commands can be:
#   "up", "down", "left", "right". If the command is invalid, you should ignore it.
#   The player moves in the given direction with one step for each command and collects all the coins that come across.
#   If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
#   Note: He can go through the same path many times, but he can collect the coins just once (the first time).
#   There are only two possible outcomes of the game:
#   •	The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest
#       number.
#   •	The player collects at least 100 coins and wins the game.
#   For more clarifications, see the examples below.
#   Input
#   •	A number representing the size of the field (matrix NxN)
#   •	A matrix representing the field (each position separated by a single space)
#   •	On each of the following lines, you will get a move command.
#   Output
#   •	If the player won the game, print: "You won! You've collected {total_coins} coins."
#   •	If the player loses the game, print: "Game over! You've collected {total_coins} coins."
#   •	Collected coins have to be rounded down to the next-lowest number.
#   •	The player's path as coordinates in lists on separate lines:
#       "Your path:
#       [{row_position1}, {column_position1}]
#       [{row_position2}, {column_position2}]
#       …
#       [{row_positionN}, {column_positionN}]"
#   Constrains
#   •	There will be no case in which less than 100 coins will be in the field
#   •	All given numbers will be valid integers in the range [0, 100]

size = int(input())

field = []
my_path = []
player_pos = []
coins = 0

for i in range(size):
    row = [int(x) if x.isdigit() else str(x) for x in input().split()]
    field.append(row)

    if "P" in row:
        player_pos = [i, row.index("P")]

directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

my_path.append(player_pos)

while coins < 100:
    command = input()
    if command in ["up", "down", "left", "right"]:

        row, col = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]
        if row < 0:
            row = size - 1
        elif row == size:
            row = 0
        if col < 0:
            col = size - 1
        elif col == size:
            col = 0

        if field[row][col] == "X":
            coins //= 2
            my_path.append([row, col])
            break

        elif field[row][col] == "P":
            my_path.append([row, col])
            player_pos = [row, col]
            continue

        else:
            coins += field[row][col]
            field[row][col] = 0
            my_path.append([row, col])
            player_pos = [row, col]


if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
for pos in my_path:
    print(pos)

