#   Your task is to collect as many eggs as possible.
#   On the first line, you will be given a number representing the size of the field. On the following few lines, you
#   will be given a field with:
#   •	One bunny - randomly placed in it and marked with the symbol "B"
#   •	Number of eggs placed at different positions of the field and traps marked with "X"
#   Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The
#   directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking
#   some of the directions, you should not consider the fields after the trap in this direction. For more
#   clarifications, see the examples below.
#   Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
#   Input
#   •	A number representing the size of the field
#   •	The matrix representing the field (each position separated by a single space)
#   Output
#   •	The direction which should be considered as best (lowercase)
#   •	The field positions from which we are collecting eggs as lists
#   •	The total number of eggs collected
#   Constraints
#   •	There will NOT be two or more paths consisting of the same total amount of eggs.

size = int(input())

matrix = []
bunny_pos = []
best_path = []

best_direction = None
max_collected_eggs = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

for direction, positions in directions.items():
    row, col = [
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1],
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_collected_eggs:
        best_direction = direction
        max_collected_eggs = collected_eggs
        best_path = path

print(best_direction)
print(*best_path, sep="\n")
print(max_collected_eggs)
