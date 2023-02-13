#   You will be given a string. Then, you will be given an integer N for the size of the field with square shape. On the
#   next N lines, you will receive the rows of the field. The player will be placed on a random position, marked with
#   "P". On random positions there will be letters. All of the empty positions will be marked with "-".
#   Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it,
#   concatenates it to the initial string and the letter disappears from the field. If he tries to move outside of the
#   field, he is punished - he loses the last letter in the string, if there are any, and the player’s position is not
#   changed.
#   At the end print all letters and the field.
#   Input
#   •	On the first line, you are given the initial string
#   •	On the second line, you are given the integer N - the size of the square matrix
#   •	The next N lines holds the values for every row
#   •	On the next line you receive a number M
#   •	On the next M lines you will get a move command
#   Output
#   •	On the first line the final state of the string
#   •	In the end print the matrix
#   Constraints
#   •	The size of the square matrix will be between [2…10]
#   •	The player position will be marked with "P"
#   •	The letters on the field will be any letter except for "P"
#   •	Move commands will be: "up", "down", "left", "right"

initial_string = input()
size = int(input())
field = []
player_pos = []

for i in range(size):
    row = list(input())
    field.append(row)
    if "P" in row:
        player_pos = [i, row.index("P")]

nr_of_commands = int(input())

directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

for _ in range(nr_of_commands):
    command = input()
    row, col = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]

    if not 0 <= row < size or not 0 <= col < size:
        initial_string = initial_string[:-1]
        continue

    if field[row][col] != "-":
        initial_string += field[row][col]

    field[player_pos[0]][player_pos[1]] = "-"
    player_pos = [row, col]
    field[row][col] = "P"

print(initial_string)
for row in field:
    print(*row, sep="")



