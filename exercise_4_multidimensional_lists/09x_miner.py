#   You are going to create a game called "Miner".
#   First, you will receive the size of a square field in which the miner should move.
#   On the second line, you will receive the commands for the miner's movement, separated by a single space. The
#   possible commands are "left", "right", "up" and "down".
#   In the end, you will receive each row of the field on a separate line. The possible characters that may appear on
#   the screen are:
#   •	* - a regular position on the field
#   •	e - the end of the route
#   •	c - coal
#   •	s - miner
#   The miner starts moving from the position "s". He should perform the given commands successively, moving with only
#   one position in the given direction. If the miner has reached the edge of the field and the following command
#   indicates that he has to get out of the area, he must remain in his current position and ignore the command.
#   When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end,
#   you should print whether the miner has succeeded in collecting the coal or not and his final position:
#   •	If the miner has collected all coal in the field, the program stops, and you should print the message:
#       "You collected all coal! ({row_index}, {col_index})".
#   •	If the miner steps at "e", the game is over (the program stops), and you should print the message:
#       "Game over! ({row_index}, {col_index})".
#   •	If there are no more commands and none of the above cases had happened, you should print the message:
#       "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
#   Input
#   •	Field size - an integer number
#   •	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
#   •	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
#   Output
#   •	There are three types of output as mentioned above.
#   Constraints
#   •	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
#   •	The field will always have only one "s"

field_size = int(input())
directions = input().split()
mine_map = [input().split() for row in range(field_size)]

miner_position = ()
for row in range(len(mine_map)):
    for col in range(len(mine_map)):
        if mine_map[row][col] == "s":
            miner_position = (row, col)

coal_to_collect = 0
for row in mine_map:
    for col in row:
        if col == "c":
            coal_to_collect += 1

possible_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

game_ended = False

for command in directions:
    x, y = possible_directions[command]
    r, c = miner_position[0] + x, miner_position[1] + y
    if 0 <= r < field_size and 0 <= c < field_size:
        mine_map[miner_position[0]][miner_position[1]] = "*"
        miner_position = (r, c)
        if mine_map[r][c] == "e":
            game_ended = True
            print(f"Game over! {miner_position}")
            break
        if mine_map[r][c] == "c":
            coal_to_collect -= 1
            if coal_to_collect == 0:
                print(f"You collected all coal! {miner_position}")
                break
        mine_map[r][c] = "s"

if not game_ended and coal_to_collect:
    print(f"{coal_to_collect} pieces of coal left. {miner_position}")


