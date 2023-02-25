rows, cols = [int(x) for x in input().split()]

playground = []
player_pos = []
touched_players = 0
moves_made = 0

for i in range(rows):
    row = input().split()
    playground.append(row)
    if "B" in row:
        player_pos = [i, row.index("B")]

directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

while True:
    command = input()
    if command == "Finish":
        break
    if touched_players == 3:
        break

    row, col = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]

    if 0 <= row < rows and 0 <= col < cols:
        if playground[row][col] != "O":

            if playground[row][col] == "P":
                touched_players += 1
                moves_made += 1
            elif playground[row][col] == "-":
                moves_made += 1
            playground[player_pos[0]][player_pos[1]] = "-"
            playground[row][col] = "B"
            player_pos = [row, col]


print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves_made}")
