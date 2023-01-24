#   You are participating in a Firearm course. It is a training day at the shooting range.
#   You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by
#   a single space:
#   •	Your position is marked with the symbol "A"
#   •	Targets marked with symbol "x"
#   •	All of the empty positions will be marked with "."
#   After the field state, you will be given an integer representing the number of commands you will receive. The
#   possible commands are:
#   •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only
#       move if the field you want to step on is marked with ".".
#   •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without
#       moving). Beware that there might be targets that stand in the way of other targets, and you cannot reach them -
#       you can shoot only the nearest target. When you have shot a target, the field becomes empty position (".").
#   Validate the positions since they can be outside the field.
#   Keep track of all the shot targets:
#   •	If at any point there are no targets left, end the program and print:
#       "Training completed! All {count_targets} targets hit.".
#   •	If, after you perform all the commands, there are some targets left print:
#       "Training not completed! {count_left_targets} targets left.".
#   Finally, print the index positions of the targets that you hit, as shown in the examples.
#   Input
#   •	5 lines representing the field (symbols, separated by a single space)
#   •	N - count of commands
#   •	On the following N lines - the commands in the format described above
#   Output
#   •	On the first line, print one of the following:
#       o	If all the targets were shot:
#       "Training completed! All {count_targets} targets hit."
#       o	Otherwise:
#       "Training not completed! {count_left_targets} targets left."
#   •	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
#   Constrains
#   •	All the commands will be valid
#   •	There will always be at least one target

shooting_range = []
player_pos = []
nr_of_targets = 0
targets_hit = 0
shot_targets_positions = []

for row in range(5):
    shooting_range.append(input().split())

    if "A" in shooting_range[row]:
        player_pos = [row, shooting_range[row].index("A")]

    if "x" in shooting_range[row]:
        nr_of_targets += shooting_range[row].count("x")

directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

nr_of_commands = int(input())
all_targets_hit = False

for _ in range(nr_of_commands):
    current_command = input().split()
    action = current_command[0]
    direction = current_command[1]

    if action == "move":
        space = int(current_command[2])
        m_row, m_col = [
            player_pos[0] + (directions[direction][0] * space),
            player_pos[1] + (directions[direction][1] * space),
        ]
        if 0 <= m_row < 5 and 0 <= m_col < 5:
            if shooting_range[m_row][m_col] != "x":
                shooting_range[player_pos[0]][player_pos[1]] = "."
                player_pos = [m_row, m_col]
                shooting_range[m_row][m_col] = "A"

    elif action == "shoot":
        s_row, s_col = [
            player_pos[0] + directions[direction][0],
            player_pos[1] + directions[direction][1],
        ]
        while 0 <= s_row < 5 and 0 <= s_col < 5:
            if shooting_range[s_row][s_col] == "x":
                shooting_range[s_row][s_col] = "."
                targets_hit += 1
                shot_targets_positions.append([s_row, s_col])
                if nr_of_targets == targets_hit:
                    print(f"Training completed! All {targets_hit} targets hit.")
                    all_targets_hit = True
                    break
                break
            else:
                s_row += directions[direction][0]
                s_col += directions[direction][1]

    if all_targets_hit:
        break

if not all_targets_hit:
    print(f"Training not completed! {nr_of_targets - targets_hit} targets left.")

for target in shot_targets_positions:
    print(target)
